"""提供经量表负责人确认的题目对应关系。"""


def confirmed_mappings(records):
    return [
        row for row in records
        if row.get("kind") == "mapping" and row.get("status") == "confirmed"
        and row.get("from_item") and row.get("to_item") and row.get("common_construct")
    ]
