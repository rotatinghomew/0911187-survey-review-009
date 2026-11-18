import unittest

from survey_review.analysis import summarize
from survey_review.reports import build_report


class SurveyReviewTests(unittest.TestCase):
    def setUp(self):
        self.records = [
            {"id": "i1", "kind": "item", "version": "v1", "construct": "自主性", "text": "独立提出问题"},
            {"id": "i2", "kind": "item", "version": "v2", "construct": "规划能力", "text": "规划研究步骤"},
            {"id": "r1", "kind": "response", "version": "v1", "item_id": "i1", "student_id": "s1", "value": 4, "status": "valid"},
            {"id": "r2", "kind": "response", "version": "v2", "item_id": "i2", "student_id": "s1", "value": 5, "status": "valid"},
            {"id": "r3", "kind": "response", "version": "v2", "item_id": "i2", "student_id": "s2", "value": None, "status": "withdrawn"},
            {"id": "s1", "kind": "stage", "student_id": "s1", "stage": "中期"},
            {"id": "m1", "kind": "mapping", "from_item": "i1", "to_item": "i2", "common_construct": "自主研究", "status": "proposed"},
        ]

    def test_unconfirmed_mapping_does_not_join_different_items(self):
        result = summarize(self.records)
        self.assertEqual(len(result["items"]), 2)
        self.assertEqual(result["confirmed_mappings"], [])

    def test_withdrawn_answers_are_excluded_and_visible(self):
        report = build_report(self.records, "survey-r4")
        self.assertEqual(report["withdrawn_responses"], ["r3"])
        self.assertEqual(report["analysis"]["items"]["v2:i2"]["valid_responses"], 1)


if __name__ == "__main__":
    unittest.main()
