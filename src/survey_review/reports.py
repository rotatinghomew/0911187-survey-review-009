"""可追溯的当前汇总报告。"""

from .analysis import summarize


def build_report(records, source_revision=""):
    if not source_revision:
        raise ValueError("必须提供数据修订标识")
    return {
        "source_revision": source_revision,
        "record_count": len(records),
        "analysis": summarize(records),
        "withdrawn_responses": sorted(row["id"] for row in records if row["kind"] == "response" and row.get("status") == "withdrawn"),
    }
