import re

text = """Spud AC-857 #2 on 6/14, prior screen issues on AC-25.
Crew transferred from GC654 mid-hitch. FRAC-99 stage complete.
Mobilizing to MC-2871 next. PO-4471 approved for tools.
Note: AC-9021 logged but see ticket P0-3344 for the discrepancy."""

pattern = r"\b[A-Z]{2}-\d{2,4}\b"

all_matches = re.findall(pattern, text)
first_match = re.search(pattern, text)

print(all_matches)
print(first_match)