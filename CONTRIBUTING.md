# Contributing / Como contribuir

Issues and pull requests are welcome, in English or Portuguese.
Issues e pull requests são bem-vindos, em inglês ou português.

## What helps most / O que mais ajuda

- New entries in `skills/bks-daiwl/references/fundamentals-catalog.md`, with EN/PT aliases and a primary source.
- Translations of user-facing strings (the `I18N` table in `skills/bks-daiwl/scripts/daiwl.py`).
- New source readers (`skills/bks-daiwl/references/sources.md`).
- Bug reports with the `findings.json` that produced the wrong score.

## Rules / Regras

- Internal keys, JSON fields and `.daiwl/` folder names stay in English.
- `scripts/daiwl.py` uses the Python standard library only (3.9+). No new dependency without discussion.
- Changing weights or factors bumps `formula_version` and needs a `CHANGELOG.md` entry.
- Never commit a real vault, notes or reports: they may contain personal data.

## Pull requests

1. Fork, create a branch from `main`.
2. Keep the change focused; update `CHANGELOG.md` under `[Unreleased]`.
3. Run `python -m unittest discover -s tests` (standard library only, no install needed).
