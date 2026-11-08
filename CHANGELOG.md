# Changelog

All notable changes to BKS-DAIWL. Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [SemVer](https://semver.org/) — MAJOR for breaking changes in the vault/findings format or commands,
MINOR for new commands/features, PATCH for fixes and wording. The score formula has its own version
(`formula_version`); changing weights or factors bumps it, and reports refuse to show a delta across formulas.

## [Unreleased]
### Changed
- Repository layout: the skill lives in `skills/bks-daiwl/`; README, CHANGELOG and license at the root.

## [1.0.0] — 2026-11-07
### Added
- Bilingual skill (English and Portuguese): commands accepted in both languages, reports, vault scaffold and notes
  generated in the user's language (`--lang en|pt-BR` or `language` in `config.md`).
- `README.md` (English) and `README.pt-BR.md`.
- Versioning: `VERSION`, `metadata.version` in `SKILL.md`, `daiwl version`, `skill_version` and `formula_version`
  stored in every `score.json` and shown in reports.
- Delta between analyses is suppressed when the formula version differs.
### Changed (breaking)
- Internal keys and `.daiwl/` folders are now English: `index.md`, `learnings/`, `experiences/`, `history/`;
  `findings.json` uses `fundamentals`, `class` (`aligned|gap|divergent|unfounded`), `level`
  (`masters|knows|declared|learned|experience`). Score abbreviation: PMS (EN) / SMP (PT).
- Script renamed commands: `sources`, `inventory`; flags `--create`, `--source`, `--lang`
  (Portuguese aliases `fontes`, `inventario`, `versao`, `--criar`, `--fonte`, `--idioma` still work).
- Source types `repo`, `notes`, `papers`; authorship `own|mixed|ai` (aliases `repositorio`, `notas`, `artigos`,
  `propria`, `mista`).
### Migration from 0.x
- `findings.json` in the old Portuguese schema is normalized automatically by `score`/`rescore`.
- `rescore` also reads old `aprendizados/` and `experiencias/` folders and old frontmatter keys.
- Rename `.daiwl/indice.md` → `index.md` and `historico/` → `history/` (or keep them; nothing is deleted).

## [0.3.0] — 2026-11-07
### Added
- `init` (create a vault or register existing sources), `fontes`, `inventario`; source types and repository authorship;
  `declarado` level.

## [0.2.0] — 2026-11-07
### Changed
- Renamed from "Cânone Essencial" to `bks-daiwl`.

## [0.1.0] — 2026-11-07
### Added
- First draft: `indexar`, `analisar`, `aprendi`, `experiencia`; deterministic score; MD/HTML reports.
