"""读取量表题目版本、答卷状态和培养阶段事实。"""

import json
from pathlib import Path


def load_records(path):
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise ValueError("记录文件必须包含数组")
    records = []
    seen = set()
    for position, record in enumerate(payload):
        if not isinstance(record, dict) or not record.get("id") or record.get("kind") not in {"item", "response", "stage", "mapping"}:
            raise ValueError(f"第 {position + 1} 条测量记录缺少身份或类型")
        if record["id"] in seen:
            raise ValueError(f"重复记录标识：{record['id']}")
        seen.add(record["id"])
        if record["kind"] in {"item", "response"} and not record.get("version"):
            raise ValueError(f"记录 {record['id']} 缺少量表版本")
        records.append(dict(record))
    return records
