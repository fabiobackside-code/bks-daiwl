"""Gera dist/bks-daiwl-<versão>.skill, o pacote instalável no Claude.ai e no Claude Desktop."""
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "bks-daiwl"
SKIP = {"__pycache__", ".daiwl"}


def main():
    version = (SKILL / "VERSION").read_text(encoding="utf-8").strip()
    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)
    target = dist / f"bks-daiwl-{version}.skill"
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as z:
        for path in sorted(SKILL.rglob("*")):
            if path.is_file() and not SKIP.intersection(path.parts):
                z.write(path, Path("bks-daiwl") / path.relative_to(SKILL))
        for extra in ("README.md", "README.pt-BR.md", "CHANGELOG.md", "LICENSE"):
            z.write(ROOT / extra, Path("bks-daiwl") / extra)
    print(target)


if __name__ == "__main__":
    sys.exit(main())
