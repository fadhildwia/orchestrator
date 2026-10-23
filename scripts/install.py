#!/usr/bin/env python3
"""Plan or install the four product workflow skills and Codex agent files."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import sys
import tempfile
from datetime import datetime, timezone
import uuid


SKILLS = (
    "product-orchestrator",
    "critical-product-research",
    "product-ui-ux",
    "product-review-qa",
)
AGENTS = (
    "product_orchestrator.toml",
    "product_researcher.toml",
    "product_designer.toml",
    "product_reviewer.toml",
)


class InstallError(Exception):
    """An unsafe or conflicting installation; no preflight changes are written."""


def _absolute(path: Path | str) -> Path:
    return Path(os.path.abspath(Path(path).expanduser()))


def _hash(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _is_link(path: Path) -> bool:
    if path.is_symlink():
        return True
    try:
        # Windows junctions are reparse points, although is_symlink() is false.
        attributes = getattr(path.lstat(), "st_file_attributes", 0)
        return bool(attributes & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0))
    except FileNotFoundError:
        return False


def _safe_path(path: Path, anchor: Path, *, directory: bool = False) -> None:
    """Reject symlinks and non-directory parents without resolving them away."""
    try:
        parts = path.relative_to(anchor).parts
    except ValueError as exc:
        raise InstallError(f"Path escapes its installation root: {path}") from exc
    current = anchor
    for index in range(len(parts) + 1):
        if _is_link(current):
            raise InstallError(f"Symlink is not allowed in an owned path: {current}")
        final = index == len(parts)
        if current.exists():
            expected_dir = not final or directory
            if expected_dir and not current.is_dir():
                raise InstallError(f"Expected directory: {current}")
            if final and not directory and not current.is_file():
                raise InstallError(f"Expected regular file: {current}")
        if not final:
            current = current / parts[index]


def _target(key: str, codex_home: Path, skills_home: Path) -> Path:
    if not isinstance(key, str) or "\\" in key or ":" in key:
        raise InstallError("Invalid managed file name in manifest or source")
    logical = PurePosixPath(key)
    if logical.is_absolute() or logical.as_posix() != key:
        raise InstallError(f"Invalid managed file name: {key}")
    if any(part in (".", "..", "") for part in logical.parts):
        raise InstallError(f"Invalid managed file name: {key}")
    parts = logical.parts
    if len(parts) >= 3 and parts[0] == "skills" and parts[1] in SKILLS:
        return skills_home.joinpath(*parts[1:])
    if len(parts) == 2 and parts[0] == "agents" and parts[1] in AGENTS:
        return codex_home.joinpath(*parts)
    raise InstallError(f"File is outside the known skills and agents: {key}")


def _read_sources(package_root: Path) -> dict[str, bytes]:
    files: dict[str, bytes] = {}
    def inaccessible(error: OSError) -> None:
        raise InstallError(f"Cannot inspect source directory: {error}") from error

    for skill in SKILLS:
        root = package_root / "skills" / skill
        _safe_path(root, package_root, directory=True)
        if not (root / "SKILL.md").is_file():
            raise InstallError(f"Required skill is missing: {root / 'SKILL.md'}")
        for current, dirs, names in os.walk(root, followlinks=False, onerror=inaccessible):
            for name in dirs + names:
                entry = Path(current) / name
                if _is_link(entry):
                    raise InstallError(f"Source symlink is not allowed: {entry}")
            for name in names:
                source = Path(current) / name
                _safe_path(source, package_root)
                files[source.relative_to(package_root).as_posix()] = source.read_bytes()
    for agent in AGENTS:
        source = package_root / "agents" / agent
        _safe_path(source, package_root)
        if not source.is_file():
            raise InstallError(f"Required agent is missing: {source}")
        files[f"agents/{agent}"] = source.read_bytes()
    if len({key.casefold() for key in files}) != len(files):
        raise InstallError("Source contains file names differing only by case")
    return dict(sorted(files.items()))


def _unique_json(pairs: list[tuple[str, object]]) -> dict:
    result: dict = {}
    for key, value in pairs:
        if key in result:
            raise InstallError(f"Duplicate key in installation manifest: {key}")
        result[key] = value
    return result


def _read_manifest(path: Path, codex_home: Path, skills_home: Path) -> dict[str, str]:
    _safe_path(path, codex_home)
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_unique_json)
    except (OSError, ValueError) as exc:
        raise InstallError(f"Cannot read installation manifest: {exc}") from exc
    if (
        not isinstance(data, dict)
        or set(data) != {"version", "skills_home", "files"}
        or type(data["version"]) is not int
        or data["version"] != 1
        or data["skills_home"] != str(skills_home)
        or not isinstance(data["files"], dict)
    ):
        raise InstallError("Invalid manifest schema or a different --skills-home")
    files = data["files"]
    if len({key.casefold() for key in files}) != len(files):
        raise InstallError("Manifest has file names differing only by case")
    for key, digest in files.items():
        destination = _target(key, codex_home, skills_home)
        anchor = skills_home if key.startswith("skills/") else codex_home
        _safe_path(destination, anchor)
        if not isinstance(digest, str) or re.fullmatch(r"[0-9a-f]{64}", digest) is None:
            raise InstallError(f"Invalid hash in installation manifest: {key}")
    return files


def _atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(prefix=".product-workflow-", dir=path.parent, delete=False) as output:
            temporary = Path(output.name)
            output.write(data)
            output.flush()
            os.fsync(output.fileno())
        os.replace(temporary, path)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()


def run_install(
    package_root: Path,
    codex_home: Path,
    skills_home: Path | None = None,
    *,
    apply: bool = False,
) -> dict[str, object]:
    """Preflight every owned path before writing. Return a small plan/result."""
    package_root = _absolute(package_root)
    codex_home = _absolute(codex_home)
    skills_home = _absolute(skills_home) if skills_home is not None else codex_home / "skills"
    state_root = codex_home / "product-workflow"
    manifest_path = state_root / "manifest.json"
    _safe_path(codex_home, codex_home, directory=True)
    _safe_path(skills_home, skills_home, directory=True)
    _safe_path(state_root / "backups", codex_home, directory=True)
    sources = _read_sources(package_root)
    previous = _read_manifest(manifest_path, codex_home, skills_home)
    original_manifest = manifest_path.read_bytes() if manifest_path.exists() else None
    updated = dict(previous)
    changes: list[tuple[str, Path, bytes, bytes | None]] = []
    snapshots: dict[Path, bytes | None] = {}
    same = 0
    for key, desired in sources.items():
        destination = _target(key, codex_home, skills_home)
        anchor = skills_home if key.startswith("skills/") else codex_home
        _safe_path(destination, anchor)
        current = destination.read_bytes() if destination.exists() else None
        snapshots[destination] = current
        digest = _hash(desired)
        if current == desired:
            same += 1
        elif current is not None:
            if key not in previous:
                raise InstallError(f"Unmanaged file differs; leaving it unchanged: {destination}")
            if _hash(current) != previous[key]:
                raise InstallError(f"Managed file was edited; leaving it unchanged: {destination}")
            changes.append((key, destination, desired, current))
        else:
            changes.append((key, destination, desired, None))
        updated[key] = digest
    manifest_bytes = (json.dumps({"version": 1, "skills_home": str(skills_home), "files": updated},
                                 ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")
    result: dict[str, object] = {
        "apply": apply, "changed": len(changes), "unchanged": same,
        "manifest_changed": manifest_bytes != original_manifest,
    }
    if not apply:
        return result

    # Recheck snapshots immediately before mutations to catch intervening edits.
    for destination, snapshot in snapshots.items():
        anchor = skills_home if destination.is_relative_to(skills_home) else codex_home
        _safe_path(destination, anchor)
        current = destination.read_bytes() if destination.exists() else None
        if current != snapshot:
            raise InstallError(f"File changed during preflight: {destination}")
    _safe_path(manifest_path, codex_home)
    if (manifest_path.read_bytes() if manifest_path.exists() else None) != original_manifest:
        raise InstallError("Installation manifest changed during preflight")
    backup_root = state_root / "backups" / (
        datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-" + uuid.uuid4().hex[:12]
    )
    for key, _, _, old in changes:
        if old is not None:
            backup = backup_root.joinpath(*PurePosixPath(key).parts)
            _safe_path(backup, codex_home)
            _atomic_write(backup, old)
    for key, destination, desired, _ in changes:
        anchor = skills_home if key.startswith("skills/") else codex_home
        _safe_path(destination, anchor)
        _atomic_write(destination, desired)
    if manifest_bytes != original_manifest:
        _safe_path(manifest_path, codex_home)
        _atomic_write(manifest_path, manifest_bytes)
    return result


def main(argv: list[str] | None = None, *, package_root: Path | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--codex-home", type=Path, default=Path(os.environ.get("CODEX_HOME") or "~/.codex"))
    parser.add_argument("--skills-home", type=Path, help="Override the skill destination; agents still use CODEX_HOME/agents")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true", help="Write the plan; default is read-only")
    mode.add_argument("--dry-run", action="store_true", help="Show the plan without writing (default)")
    args = parser.parse_args(argv)
    try:
        source_root = package_root if package_root is not None else Path(__file__).resolve().parents[1]
        result = run_install(source_root, args.codex_home, args.skills_home, apply=args.apply)
    except (InstallError, OSError) as exc:
        print(f"Installation stopped: {exc}", file=sys.stderr)
        return 1
    action = "Installed" if args.apply else "Plan (no writes)"
    print(f"{action}: {result['changed']} file(s) to write, {result['unchanged']} already match.")
    if not args.apply:
        print("Run again with --apply to install. config.toml and AGENTS.md are untouched.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
