"""合成业务记录的读取和基础校验。"""

import json
from pathlib import Path


def load_records(path):
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise ValueError("记录文件必须包含数组")
    records = []
    seen = set()
    for position, record in enumerate(payload):
        if not isinstance(record, dict) or not record.get("id"):
            raise ValueError(f"第 {position + 1} 条记录缺少 id")
        if record["id"] in seen:
            raise ValueError(f"重复记录标识：{record['id']}")
        seen.add(record["id"])
        records.append(dict(record))
    return records
