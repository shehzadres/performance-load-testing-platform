import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "analyze.py"
SPEC = importlib.util.spec_from_file_location("analyze", MODULE_PATH)
ANALYZE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ANALYZE)


class PercentileTests(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(ANALYZE.pct([], 0.95), 0.0)

    def test_single_value(self):
        self.assertEqual(ANALYZE.pct([42], 0.95), 42.0)

    def test_interpolated_median(self):
        self.assertEqual(ANALYZE.pct([10, 20], 0.5), 15.0)

    def test_p95_bounds(self):
        result = ANALYZE.pct(list(range(1, 101)), 0.95)
        self.assertGreaterEqual(result, 95)
        self.assertLessEqual(result, 96)


class AnalyzerCliTests(unittest.TestCase):
    def test_cli_writes_summary_report_and_showcase_data(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            fixture = root / "fixture.jtl"
            fixture.write_text(
                "timeStamp,elapsed,label,responseCode,success\n"
                "1000,100,Health,200,true\n"
                "1100,200,Products,200,true\n"
                "1300,300,Checkout,201,true\n",
                encoding="utf-8"
            )
            subprocess.run(
                [sys.executable, str(MODULE_PATH), "--input", str(fixture), "--run-id", "unit-fixture"],
                cwd=root, check=True, capture_output=True, text=True
            )
            summary = json.loads((root / "results/unit-fixture.json").read_text(encoding="utf-8"))
            latest = json.loads((root / "showcase/data/latest.json").read_text(encoding="utf-8"))
            report = (root / "reports/unit-fixture.md").read_text(encoding="utf-8")
            self.assertEqual(summary["sample_count"], 3)
            self.assertEqual(summary["failed_samples"], 0)
            self.assertEqual(latest["run_id"], "unit-fixture")
            self.assertIn("Response time", report)


if __name__ == "__main__":
    unittest.main()
