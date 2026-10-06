import csv
from io import StringIO


def validate_csv_content(file_content: str):
    try:
        csv_reader = csv.DictReader(StringIO(file_content))
        if not csv_reader.fieldnames:
            return False, [], [{"message": "CSV file is empty"}]

        required_fields = {"Word", "Meaning", "IpaUk", "IpaUs", "ExampleEn", "ExampleVn", "Topic"}
        if not required_fields.issubset(set(csv_reader.fieldnames)):
            missing = required_fields - set(csv_reader.fieldnames)
            return False, [], [{"message": f"Missing required columns: {', '.join(sorted(missing))}"}]

        rows = []
        errors = []

        for row_index, row in enumerate(csv_reader, start=2):
            if not (row.get("Word") or "").strip():
                errors.append({"row": row_index, "message": "Word is required"})
                continue
            if not (row.get("Meaning") or "").strip():
                errors.append({"row": row_index, "message": "Meaning is required"})
                continue
            if not (row.get("Topic") or "").strip():
                errors.append({"row": row_index, "message": "Topic is required"})
                continue
            rows.append(row)

        return True, rows, errors
    except Exception as exc:
        return False, [], [{"message": f"Error parsing CSV: {str(exc)}"}]


def normalize_text(value: str) -> str:
    if value is None:
        return ""
    return " ".join(value.lower().strip().split())
