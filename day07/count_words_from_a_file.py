import sys
from pathlib import Path
from collections import Counter

# --- 1. Parse command-line argument ---
if len(sys.argv) != 2:
    print(f"Usage: {Path(sys.argv[0]).name} <input_file>", file=sys.stderr)
    sys.exit(1)

in_path = Path(sys.argv[1])
if not in_path.is_file():
    print(f"ERROR: {in_path} not found.", file=sys.stderr)
    sys.exit(1)

# --- 2. Read, normalise, and count words (case-insensitive) ---
text = in_path.read_text(encoding="utf-8")
words = text.lower().split()          # split on any whitespace
counts = Counter(words)               # {'ad': 13, 'labor': 10, ...}

# --- 3. Prepare output file path ---
out_path = in_path.with_stem(f"{in_path.stem}_counted")

# --- 4. Write results sorted alphabetically, nicely aligned ---
max_word_len = max(len(w) for w in counts)
with out_path.open("w", encoding="utf-8") as fh:
    for word in sorted(counts):
        fh.write(f"{word.ljust(max_word_len + 2)}{counts[word]}\n")

print(f"Done! Results written to {out_path}")
