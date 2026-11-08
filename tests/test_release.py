"""Guarda de release: a versão anda junta nos quatro lugares e o pacote sai completo."""
import re
import subprocess
import sys
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "bks-daiwl"


def version_file():
    return (SKILL / "VERSION").read_text(encoding="utf-8").strip()


class VersionTests(unittest.TestCase):
    def test_skill_md_metadata_matches(self):
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn(f'version: "{version_file()}"', text)

    def test_script_constant_matches(self):
        text = (SKILL / "scripts" / "daiwl.py").read_text(encoding="utf-8")
        self.assertIn(f'SKILL_VERSION = "{version_file()}"', text)

    def test_changelog_has_entry(self):
        text = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        self.assertRegex(text, rf"## \[{re.escape(version_file())}\]")

    def test_readme_badges_match(self):
        for name in ("README.md", "README.pt-BR.md"):
            self.assertIn(f"-{version_file()}-", (ROOT / name).read_text(encoding="utf-8"), name)


class PackageTests(unittest.TestCase):
    def test_package_contains_skill_and_license(self):
        out = subprocess.run([sys.executable, str(ROOT / "scripts" / "package.py")],
                             capture_output=True, text=True, check=True)
        names = zipfile.ZipFile(out.stdout.strip()).namelist()
        for required in ("bks-daiwl/SKILL.md", "bks-daiwl/scripts/daiwl.py", "bks-daiwl/LICENSE",
                         "bks-daiwl/references/score.md"):
            self.assertIn(required, names)
        self.assertFalse(any("__pycache__" in n for n in names))


if __name__ == "__main__":
    unittest.main()
