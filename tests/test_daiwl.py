"""Testes do daiwl.py: pontuação determinística, normalização do esquema antigo e CLI."""
import importlib.util
import json
import math
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "skills" / "bks-daiwl" / "scripts" / "daiwl.py"
spec = importlib.util.spec_from_file_location("daiwl", SCRIPT)
daiwl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(daiwl)


def fundamental(name, cls, weight=3, occurrences=1, **extra):
    f = {"name": name, "category": "Test", "weight": weight, "class": cls,
         "occurrences": [{"file": "a.cs", "line": i + 1, "snippet": "x"} for i in range(occurrences)]}
    f.update(extra)
    return f


def run_cli(*args, cwd=None):
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    return subprocess.run([sys.executable, str(SCRIPT), *args], capture_output=True, text=True,
                          encoding="utf-8", env=env, cwd=cwd)


class FactorTests(unittest.TestCase):
    def test_aligned_masters_counts_full(self):
        self.assertEqual(daiwl.factor({"class": "aligned", "level": "masters"}), 1.0)

    def test_learned_without_confidence_counts_as_low(self):
        self.assertEqual(daiwl.factor({"class": "aligned", "level": "learned"}), 0.60)

    def test_experience_without_type_counts_as_preference(self):
        self.assertEqual(daiwl.factor({"class": "aligned", "level": "experience"}), 0.50)

    def test_negative_classes(self):
        self.assertEqual(daiwl.factor({"class": "divergent"}), -0.50)
        self.assertEqual(daiwl.factor({"class": "unfounded"}), -0.25)
        self.assertEqual(daiwl.factor({"class": "gap"}), 0.0)


class ComputeTests(unittest.TestCase):
    def test_occurrences_are_dampened_by_log(self):
        f = fundamental("Guard clause", "gap", weight=2, occurrences=30)
        self.assertAlmostEqual(daiwl.impact(f), 2 * (1 + math.log(30)))

    def test_all_mastered_scores_100(self):
        data = {"fundamentals": [fundamental("Result Pattern", "aligned", level="masters")]}
        self.assertEqual(daiwl.compute(data)["pms"], 100.0)

    def test_only_gaps_scores_zero(self):
        data = {"fundamentals": [fundamental("Saga", "gap", weight=5)]}
        result = daiwl.compute(data)
        self.assertEqual(result["pms"], 0.0)
        self.assertEqual(result["band"], "band_0")
        self.assertEqual(result["top_gaps"][0][0], "Saga")

    def test_negative_total_is_clamped_to_zero(self):
        data = {"fundamentals": [fundamental("Generic repository", "divergent", weight=4)]}
        self.assertEqual(daiwl.compute(data)["pms"], 0.0)

    def test_mixed_score_is_deterministic(self):
        data = {"fundamentals": [
            fundamental("Hexagonal", "aligned", weight=5, level="masters"),
            fundamental("Outbox", "gap", weight=4),
            fundamental("Retry", "aligned", weight=3, level="knows"),
        ]}
        expected = round((5 * 1.0 + 4 * 0.0 + 3 * 0.8) / 12 * 100, 1)
        self.assertEqual(daiwl.compute(data)["pms"], expected)
        self.assertEqual(daiwl.compute(data), daiwl.compute(data))

    def test_result_carries_versions(self):
        result = daiwl.compute({"fundamentals": [fundamental("X", "gap")]})
        self.assertEqual(result["skill_version"], daiwl.SKILL_VERSION)
        self.assertEqual(result["formula_version"], daiwl.FORMULA_VERSION)


class NormalizeTests(unittest.TestCase):
    def test_portuguese_schema_becomes_english(self):
        old = {"projeto": "p", "fundamentos": [{"nome": "Outbox", "peso": 4, "classe": "lacuna",
                                                 "ocorrencias": [{"arquivo": "a.cs", "linha": 1}]}]}
        new = daiwl.normalize(old)
        self.assertEqual(new["project"], "p")
        self.assertEqual(new["fundamentals"][0]["class"], "gap")
        self.assertEqual(new["fundamentals"][0]["occurrences"][0]["file"], "a.cs")

    def test_level_values_are_translated(self):
        new = daiwl.normalize({"classe": "alinhado", "nivel": "domina", "confianca": "alta"})
        self.assertEqual((new["class"], new["level"], new["confidence"]), ("aligned", "masters", "high"))


class CliTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def write_findings(self, name, fundamentals):
        path = self.root / name
        path.write_text(json.dumps({"project": "demo", "fundamentals": fundamentals}), encoding="utf-8")
        return path

    def test_version(self):
        out = run_cli("version")
        self.assertEqual(out.returncode, 0, out.stderr)
        self.assertIn(daiwl.SKILL_VERSION, out.stdout)

    def test_portuguese_alias_is_accepted(self):
        self.assertEqual(run_cli("versao").returncode, 0)

    def test_score_writes_files_and_reports_delta(self):
        history = self.root / "history"
        first = self.write_findings("f1.json", [fundamental("Outbox", "gap")])
        self.assertEqual(run_cli("score", str(first), "--out", str(history / "2026-01-01-demo")).returncode, 0)
        second = self.write_findings("f2.json", [fundamental("Outbox", "aligned", level="masters")])
        out = run_cli("score", str(second), "--out", str(history / "2026-01-02-demo"))
        self.assertEqual(out.returncode, 0, out.stderr)
        score = json.loads((history / "2026-01-02-demo" / "score.json").read_text(encoding="utf-8"))
        self.assertEqual(score["pms"], 100.0)
        self.assertEqual(score["delta_previous"], 100.0)

    def test_delta_is_suppressed_when_formula_changes(self):
        history = self.root / "history"
        old = history / "2026-01-01-demo"
        old.mkdir(parents=True)
        (old / "score.json").write_text(json.dumps({"pms": 10.0, "formula_version": "0.9"}), encoding="utf-8")
        findings = self.write_findings("f.json", [fundamental("Outbox", "aligned", level="masters")])
        run_cli("score", str(findings), "--out", str(history / "2026-01-02-demo"))
        score = json.loads((history / "2026-01-02-demo" / "score.json").read_text(encoding="utf-8"))
        self.assertIsNone(score["delta_previous"])
        self.assertEqual(score["delta_note"], "formula_changed")

    def test_init_create_scaffolds_vault_without_touching_home(self):
        vault = self.root / "vault"
        out = run_cli("init", "--vault", str(vault), "--create", "--local", "--lang", "pt-BR")
        self.assertEqual(out.returncode, 0, out.stderr)
        self.assertTrue((vault / ".daiwl" / "config.md").exists())
        self.assertTrue((vault / "Conceitos").is_dir())

    def test_repo_source_requires_authorship(self):
        out = run_cli("init", "--vault", str(self.root), "--local", "--source", "repo:/src/x")
        self.assertNotEqual(out.returncode, 0)


if __name__ == "__main__":
    unittest.main()
