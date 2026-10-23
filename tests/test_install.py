"""Exercise installation effects in disposable homes; no global Codex files."""

import importlib.util
import contextlib
import io
import hashlib
import json
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch


SPEC = importlib.util.spec_from_file_location("workflow_installer", Path(__file__).resolve().parents[1] / "scripts" / "install.py")
installer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(installer)


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.package = self.root / "package"
        self.home = self.root / "codex"
        for skill in installer.SKILLS:
            folder = self.package / "skills" / skill
            (folder / "references").mkdir(parents=True)
            (folder / "agents").mkdir()
            (folder / "SKILL.md").write_text(f"---\nname: {skill}\n---\nOriginal\n", encoding="utf-8")
            (folder / "references" / "brief.md").write_text("Supporting reference\n", encoding="utf-8")
            (folder / "agents" / "openai.yaml").write_text('interface:\n  display_name: "Example"\n', encoding="utf-8")
        templates = self.package / "skills" / "frontend-engineer" / "references" / "templates"
        templates.mkdir()
        (templates / "handoff.md").write_text("Frontend handoff template\n", encoding="utf-8")
        (self.package / "agents").mkdir()
        for name in installer.AGENTS:
            (self.package / "agents" / name).write_text(f'name = "{name[:-5]}"\n', encoding="utf-8")
        self.expected_file_count = 3 * len(installer.SKILLS) + len(installer.AGENTS) + 1

    def run_install(self, **options):
        return installer.run_install(self.package, self.home, **options)

    def snapshot(self, root=None):
        root = root or self.home
        if not root.exists():
            return {}
        return {path.relative_to(root).as_posix(): path.read_bytes() for path in root.rglob("*") if path.is_file()}

    def source(self):
        return self.package / "skills" / installer.SKILLS[0] / "SKILL.md"

    def destination(self):
        return self.home / "skills" / installer.SKILLS[0] / "SKILL.md"

    def test_default_plan_creates_nothing(self):
        result = self.run_install()
        self.assertEqual(result["changed"], self.expected_file_count)
        self.assertFalse(self.home.exists())

    def test_cli_explicit_dry_run_and_mutually_exclusive_modes(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = installer.main(["--dry-run", "--codex-home", str(self.home)], package_root=self.package)
        self.assertEqual(code, 0)
        self.assertIn("Plan (no writes)", output.getvalue())
        self.assertFalse(self.home.exists())
        with contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as error:
                installer.main(["--dry-run", "--apply"], package_root=self.package)
        self.assertEqual(error.exception.code, 2)
        self.assertFalse(self.home.exists())

    def test_install_preserves_unrelated_files_and_includes_references(self):
        unrelated = {
            "config.toml": b'model = "existing"\n',
            "AGENTS.md": b"Personal rules\n",
            "skills/my-own-skill/SKILL.md": b"Personal skill\n",
            "agents/my_agent.toml": b"Personal agent\n",
            f"skills/{installer.SKILLS[0]}/notes.txt": b"User notes\n",
        }
        for name, data in unrelated.items():
            path = self.home / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        self.run_install(apply=True)
        installed = self.snapshot()
        for name, data in unrelated.items():
            self.assertEqual(installed[name], data)
        self.assertEqual(self.destination().read_bytes(), self.source().read_bytes())
        self.assertEqual((self.destination().parent / "references" / "brief.md").read_text(), "Supporting reference\n")
        manifest = json.loads((self.home / "product-workflow" / "manifest.json").read_text())
        self.assertEqual(len(manifest["files"]), self.expected_file_count)
        self.assertNotIn("config.toml", manifest["files"])
        self.assertNotIn(f"skills/{installer.SKILLS[0]}/notes.txt", manifest["files"])

    def test_repeat_is_idempotent(self):
        self.run_install(apply=True)
        before = self.snapshot()
        result = self.run_install(apply=True)
        self.assertEqual(result["changed"], 0)
        self.assertEqual(result["unchanged"], self.expected_file_count)
        self.assertFalse(result["manifest_changed"])
        self.assertEqual(self.snapshot(), before)
        self.assertFalse((self.home / "product-workflow" / "backups").exists())

    def test_upgrade_four_skill_manifest_adds_frontend_and_preserves_personal_files(self):
        legacy_skills = tuple(skill for skill in installer.SKILLS if skill != "frontend-engineer")
        with patch.object(installer, "SKILLS", legacy_skills):
            self.run_install(apply=True)
        manifest_path = self.home / "product-workflow" / "manifest.json"
        legacy_manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        self.assertEqual(len(legacy_manifest["files"]), 16)
        unrelated = {
            "config.toml": b'model = "personal"\n',
            "AGENTS.md": b"Personal rules\n",
            "skills/personal/SKILL.md": b"Personal skill\n",
            "agents/personal.toml": b"Personal agent\n",
            "skills/frontend-engineer/references/templates/my-notes.md": b"Personal template notes\n",
        }
        for name, data in unrelated.items():
            path = self.home / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        before = self.snapshot()
        plan = self.run_install()
        self.assertEqual(plan["changed"], 4)
        self.assertEqual(plan["unchanged"], 16)
        self.assertTrue(plan["manifest_changed"])
        self.assertEqual(self.snapshot(), before)

        result = self.run_install(apply=True)
        self.assertEqual(result["changed"], 4)
        installed = self.snapshot()
        for name in (*legacy_manifest["files"], *unrelated):
            self.assertEqual(installed[name], before[name])
        nested = "skills/frontend-engineer/references/templates/handoff.md"
        self.assertEqual(installed[nested], (self.package / nested).read_bytes())
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        self.assertEqual(manifest["version"], 1)
        self.assertEqual(manifest["skills_home"], str(self.home / "skills"))
        self.assertEqual(len(manifest["files"]), self.expected_file_count)
        self.assertEqual(
            {name for name in manifest["files"] if name.startswith("agents/")},
            {f"agents/{name}" for name in installer.AGENTS},
        )
        self.assertEqual(len(installer.AGENTS), 4)
        for name, digest in manifest["files"].items():
            self.assertEqual(digest, hashlib.sha256(installed[name]).hexdigest())
        for name in unrelated:
            self.assertNotIn(name, manifest["files"])
        repeated = self.run_install(apply=True)
        self.assertEqual(repeated["changed"], 0)
        self.assertEqual(repeated["unchanged"], self.expected_file_count)
        self.assertFalse(repeated["manifest_changed"])
        self.assertEqual(self.snapshot(), installed)
        self.assertFalse((self.home / "product-workflow" / "backups").exists())

    def test_late_conflict_prevents_all_writes(self):
        conflict = self.home / "skills" / installer.SKILLS[-1] / "references" / "brief.md"
        conflict.parent.mkdir(parents=True)
        conflict.write_bytes(b"Unmanaged custom reference")
        before = self.snapshot()
        with self.assertRaisesRegex(installer.InstallError, "Unmanaged file differs"):
            self.run_install(apply=True)
        self.assertEqual(self.snapshot(), before)
        self.assertFalse((self.home / "agents").exists())

    def test_managed_upgrade_creates_backup_and_refuses_user_edits(self):
        self.run_install(apply=True)
        original = self.destination().read_bytes()
        self.source().write_bytes(b"Updated skill\n")
        self.run_install(apply=True)
        self.assertEqual(self.destination().read_bytes(), b"Updated skill\n")
        backups = list((self.home / "product-workflow" / "backups").rglob("SKILL.md"))
        self.assertEqual(len(backups), 1)
        self.assertEqual(backups[0].read_bytes(), original)
        self.destination().write_bytes(b"User changed installed skill\n")
        self.source().write_bytes(b"Another upstream version\n")
        before = self.snapshot()
        with self.assertRaisesRegex(installer.InstallError, "Managed file was edited"):
            self.run_install(apply=True)
        self.assertEqual(self.snapshot(), before)

    def test_custom_skills_home_and_matching_unmanaged_file(self):
        skill_home = self.root / "custom-skills"
        matching = skill_home / installer.SKILLS[0] / "SKILL.md"
        matching.parent.mkdir(parents=True)
        matching.write_bytes(self.source().read_bytes())
        self.run_install(skills_home=skill_home, apply=True)
        self.assertFalse((self.home / "skills").exists())
        self.assertTrue((self.home / "agents" / installer.AGENTS[0]).is_file())
        self.assertEqual(matching.read_bytes(), self.source().read_bytes())

    def test_invalid_manifest_is_refused_without_changes(self):
        state = self.home / "product-workflow"
        state.mkdir(parents=True)
        manifest = state / "manifest.json"
        invalid_cases = [
            {"version": 1, "files": {}},
            {"version": 1, "skills_home": str(self.home / "skills"), "files": {"../config.toml": "0" * 64}},
            {"version": 1, "skills_home": str(self.home / "skills"), "files": {"skills/other/SKILL.md": "0" * 64}},
            {"version": 1, "skills_home": str(self.home / "skills"), "files": {f"agents/{installer.AGENTS[0]}": "bad"}},
        ]
        for invalid in invalid_cases:
            with self.subTest(manifest=invalid):
                manifest.write_text(json.dumps(invalid))
                before = self.snapshot()
                with self.assertRaises(installer.InstallError):
                    self.run_install(apply=True)
                self.assertEqual(self.snapshot(), before)

    def test_owned_path_symlink_is_refused(self):
        external = self.root / "external"
        external.mkdir()
        skills = self.home / "skills"
        skills.mkdir(parents=True)
        try:
            (skills / installer.SKILLS[0]).symlink_to(external, target_is_directory=True)
        except (OSError, NotImplementedError):
            self.skipTest("This host does not permit symlink creation")
        with self.assertRaisesRegex(installer.InstallError, "Symlink"):
            self.run_install(apply=True)
        self.assertEqual(list(external.iterdir()), [])
        self.assertFalse((self.home / "agents").exists())

    def test_mocked_windows_reparse_point_is_rejected(self):
        # Exercise the junction guard without claiming a real Windows junction test.
        with patch.object(Path, "is_symlink", return_value=False), \
             patch.object(Path, "lstat", return_value=SimpleNamespace(st_file_attributes=0x400)), \
             patch.object(installer.stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400, create=True):
            self.assertTrue(installer._is_link(self.home))
            with self.assertRaisesRegex(installer.InstallError, "Symlink"):
                installer._safe_path(self.home, self.home, directory=True)


if __name__ == "__main__":
    unittest.main()
