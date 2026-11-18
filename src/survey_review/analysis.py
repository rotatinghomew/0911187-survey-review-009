"""培养测量审阅 的描述性汇总。"""

from collections import defaultdict


def summarize(records, group_field, value_field):
    groups = defaultdict(list)
    for record in records:
        group = record.get(group_field)
        value = record.get(value_field)
        if group is None:
            continue
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            groups[str(group)].append(float(value))
        else:
            groups[str(group)]
    result = {}
    for group, values in sorted(groups.items()):
        result[group] = {
            "observed": len(values),
            "missing": sum(1 for record in records if str(record.get(group_field)) == group and not isinstance(record.get(value_field), (int, float))),
            "mean": sum(values) / len(values) if values else None,
            "minimum": min(values) if values else None,
            "maximum": max(values) if values else None,
        }
    return result
