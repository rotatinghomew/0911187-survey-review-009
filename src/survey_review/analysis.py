"""计算各量表版本内的答卷覆盖及已确认映射。"""

from collections import defaultdict
from .comparability import confirmed_mappings


def summarize(records):
    items = {str(row["id"]): row for row in records if row["kind"] == "item"}
    responses = defaultdict(list)
    stages = {str(row["student_id"]): row for row in records if row["kind"] == "stage"}
    mappings = confirmed_mappings(records)
    for record in records:
        if record["kind"] == "response":
            responses[(str(record["version"]), str(record["item_id"]))].append(record)
    result = {}
    for (version, item_id), answers in sorted(responses.items()):
        values = [float(row["value"]) for row in answers if row.get("status") == "valid" and row.get("value") is not None]
        item = items.get(item_id, {})
        result[f"{version}:{item_id}"] = {
            "version": version,
            "item_id": item_id,
            "construct": item.get("construct"),
            "valid_responses": len(values),
            "excluded_responses": len(answers) - len(values),
            "mean": sum(values) / len(values) if values else None,
            "stage_counts": _stage_counts(answers, stages),
        }
    return {"items": result, "confirmed_mappings": [{"from": row.get("from_item"), "to": row.get("to_item"), "common_construct": row.get("common_construct")} for row in mappings]}


def _stage_counts(answers, stages):
    counts = defaultdict(int)
    for answer in answers:
        stage = stages.get(str(answer.get("student_id")), {}).get("stage", "unknown")
        counts[str(stage)] += 1
    return dict(sorted(counts.items()))
