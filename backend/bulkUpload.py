import json
from pathlib import Path
from urllib.request import Request, urlopen

url = "http://127.0.0.1:8000/items/"
data_file = Path(__file__).with_name("MOCK_DATA.json")

with data_file.open(encoding="utf-8") as file:
    records = json.load(file)

if not isinstance(records, list):
    raise ValueError("MOCK_DATA.json must contain a JSON array.")

seen_names = set()
skipped_duplicates = 0

for index, record in enumerate(records, start=1):
    name = record["Name"]
    if name in seen_names:
        skipped_duplicates += 1
        continue

    payload = {
        "name": name,
        "description": record.get("description"),
    }
    request = Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urlopen(request, timeout=10) as response:
        result = json.load(response)
    seen_names.add(name)
    print(f"Imported record {index}: {result}")

print(f"Imported {len(seen_names)} unique items; skipped {skipped_duplicates} duplicate records.")