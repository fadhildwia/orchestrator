"""Validate this setup's source files; never writes user configuration."""
from __future__ import annotations

import re
import sys
import tomllib
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml

ROOT = Path(__file__).resolve().parents[1]
ROLES = {
    "product_orchestrator": "product-orchestrator",
    "product_researcher": "critical-product-research",
    "product_designer": "product-ui-ux",
    "product_reviewer": "product-review-qa",
}
SKILLS = (*ROLES.values(), "frontend-engineer")


def validate(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    for role, skill in ROLES.items():
        profile = root / "agents" / f"{role}.toml"
        try:
            data = tomllib.loads(profile.read_text(encoding="utf-8"))
            if set(data) != {"name", "description", "developer_instructions"}:
                errors.append(f"{profile}: unexpected/missing keys")
            if data.get("name") != role:
                errors.append(f"{profile}: name mismatch")
            for key in ("description", "developer_instructions"):
                if not isinstance(data.get(key), str) or not data[key].strip():
                    errors.append(f"{profile}: {key} must be nonempty")
            if skill not in data.get("developer_instructions", ""):
                errors.append(f"{profile}: paired skill is not referenced")
        except (OSError, ValueError) as exc:
            errors.append(f"{profile}: {exc}")

    for skill in SKILLS:
        folder = root / "skills" / skill
        entry = folder / "SKILL.md"
        try:
            content = entry.read_text(encoding="utf-8")
            match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", content, re.S)
            if not match:
                raise ValueError("missing YAML frontmatter")
            frontmatter = yaml.safe_load(match[1])
            if not isinstance(frontmatter, dict) or frontmatter.get("name") != skill:
                errors.append(f"{entry}: name mismatch")
            elif not isinstance(frontmatter.get("description"), str) or not frontmatter["description"].strip():
                errors.append(f"{entry}: missing description")
            if "[TODO:" in content:
                errors.append(f"{entry}: unfinished scaffold")
            for document in (entry, *(folder / "references").rglob("*.md")):
                for link in re.findall(r"\]\(([^)\s]+)\)", document.read_text(encoding="utf-8")):
                    parsed = urlsplit(link)
                    if parsed.scheme or parsed.netloc or not parsed.path:
                        continue
                    target = (document.parent / unquote(parsed.path)).resolve()
                    if not target.is_relative_to(folder.resolve()) or not target.is_file():
                        errors.append(f"{document}: invalid reference {link}")
            ui = yaml.safe_load((folder / "agents" / "openai.yaml").read_text(encoding="utf-8"))
            interface = ui.get("interface", {}) if isinstance(ui, dict) else {}
            if not isinstance(interface.get("display_name"), str):
                errors.append(f"{folder}: missing UI display_name")
            short = interface.get("short_description", "")
            if not isinstance(short, str) or not 25 <= len(short) <= 64:
                errors.append(f"{folder}: short_description must be 25-64 chars")
        except (OSError, ValueError, yaml.YAMLError) as exc:
            errors.append(f"{entry}: {exc}")
    return errors


if __name__ == "__main__":
    issues = validate()
    for issue in issues:
        print(issue, file=sys.stderr)
    if issues:
        raise SystemExit(1)
    print(f"Validated {len(ROLES)} agent profiles, {len(SKILLS)} skills, UI metadata, and local references.")
