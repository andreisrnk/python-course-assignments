from pathlib import Path
from collections import Counter

def read_text_file(filepath):
    return Path(filepath).read_text(encoding="utf-8")

def count_digits(text):
    counts = Counter(ch for ch in text if ch.isdigit())
    return [counts.get(str(d), 0) for d in range(10)]

def write_digit_report(counts, output_path="report.txt"):
    with open(output_path, "w", encoding="utf-8") as out:
        for d, c in enumerate(counts):
            out.write(f"{d} {c}\n")
