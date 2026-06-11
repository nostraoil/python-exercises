import re

text = "Mobilized to AC-857 on 5/12. Prior job at AC-25. Crew from GC654. Frac stage FRAC-99 done. PO-1234 approved."

matches = re.findall(r"\b[A-Z]{2}-?\d+\b", text)
print(matches)