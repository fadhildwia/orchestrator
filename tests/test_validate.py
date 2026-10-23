"""Check the standalone skill and its nested documentation references."""

import importlib.util
from pathlib import Path
import tempfile
import unittest


SPEC = importlib.util.spec_from_file_location(
    "workflow_validator", Path(__file__).resolve().parents[1] / "scripts" / "validate.py"
)
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "agents").mkdir()
        for role, skill in validator.ROLES.items():
            (self.root / "agents" / f"{role}.toml").write_text(
                f'name = "{role}"\ndescription = "Role"\n'
                f'developer_instructions = "Use {skill}"\n',
                encoding="utf-8",
            )
        for skill in validator.SKILLS:
            folder = self.root / "skills" / skill
            (folder / "references" / "templates").mkdir(parents=True)
            (folder / "agents").mkdir()
            (folder / "SKILL.md").write_text(
                f"---\nname: {skill}\ndescription: Review this product artifact.\n---\n"
                "[Start](references/start.md)\n", encoding="utf-8",
            )
            (folder / "agents" / "openai.yaml").write_text(
                'interface:\n  display_name: "Example"\n'
                '  short_description: "Review a product artifact with evidence"\n',
                encoding="utf-8",
            )
            (folder / "references" / "start.md").write_text(
                "[Template](templates/handoff.md#start)\n"
                "[External](https://example.com/unavailable)\n[Section](#section)\n",
                encoding="utf-8",
            )
            (folder / "references" / "templates" / "handoff.md").write_text(
                "# Start\n[Back](../start.md)\n", encoding="utf-8",
            )
        self.frontend = self.root / "skills" / "frontend-engineer"

    def test_standalone_skill_is_valid_without_fifth_profile(self):
        self.assertEqual(len(list((self.root / "agents").glob("*.toml"))), 4)
        self.assertEqual(validator.validate(self.root), [])

    def test_missing_standalone_skill_is_reported(self):
        (self.frontend / "SKILL.md").unlink()
        errors = validator.validate(self.root)
        self.assertTrue(any("frontend-engineer" in error and "SKILL.md" in error for error in errors))

    def test_nested_missing_or_escaping_local_reference_is_reported(self):
        document = self.frontend / "references" / "templates" / "handoff.md"
        outside = self.root / "outside.md"
        outside.write_text("Not part of a skill\n", encoding="utf-8")
        for link in ("missing.md", "../../../../outside.md"):
            with self.subTest(link=link):
                document.write_text(f"[Reference]({link})\n", encoding="utf-8")
                errors = validator.validate(self.root)
                self.assertTrue(any(str(document) in error and f"invalid reference {link}" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
