"""可追溯的当前汇总报告。"""

from .analysis import summarize


def build_report(records, group_field, value_field, source_revision):
    if not source_revision:
        raise ValueError("必须提供数据修订标识")
    return {
        "source_revision": source_revision,
        "record_count": len(records),
        "groups": summarize(records, group_field, value_field),
    }
