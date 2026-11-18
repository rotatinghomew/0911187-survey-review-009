import unittest

from survey_review.analysis import summarize
from survey_review.reports import build_report


class AnalysisTests(unittest.TestCase):
    def test_groups_keep_missing_values_out_of_mean(self):
        records = [
            {"id": "a", "period": "p1", "value": 2},
            {"id": "b", "period": "p1", "value": None},
            {"id": "c", "period": "p2", "value": 6},
        ]
        result = summarize(records, "period", "value")
        self.assertEqual(result["p1"]["observed"], 1)
        self.assertEqual(result["p1"]["missing"], 1)
        self.assertEqual(result["p1"]["mean"], 2.0)

    def test_report_records_source_revision(self):
        report = build_report([{"id": "a", "period": "p1", "value": 3}], "period", "value", "rev-1")
        self.assertEqual(report["source_revision"], "rev-1")
        self.assertEqual(report["record_count"], 1)

    def test_report_requires_revision(self):
        with self.assertRaises(ValueError):
            build_report([], "period", "value", "")


if __name__ == "__main__":
    unittest.main()
