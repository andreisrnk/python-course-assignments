import sys
from pathlib import Path
from collections import Counter

if len(sys.argv) != 2:
    prog = Path(sys.argv[0]).name
    sys.exit(f"Usage: {prog} <INPUT_FILE>")

src = Path(sys.argv[1])
if not src.is_file():
    sys.exit(f"Error: '{src}' is not a regular file")

text = src.read_text(encoding="utf-8")
counts = Counter(ch for ch in text if ch.isdigit())
digit_counts = [counts.get(str(d), 0) for d in range(10)]

report_path = Path("report.txt")
with report_path.open("w", encoding="utf-8") as out:
    for d, c in enumerate(digit_counts):
        out.write(f"{d} {c}\n")

print(f"✓ Digit counts written to {report_path}")
