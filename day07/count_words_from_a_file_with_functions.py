from collections import Counter
from pathlib import Path
import sys
import re
from typing import Counter as CounterT, List

def read_sequence_file(path: Path, *, upper: bool = False) -> str:
    """Return the concatenated A-C-T-G-only string from any plain or FASTA file."""
    text = path.read_text(encoding="utf-8")
    # Remove FASTA headers and non-letters, then normalise case.
    cleaned = "\n".join(line for line in text.splitlines() if not line.startswith(">"))
    cleaned = re.sub(r"[^A-Za-z]", " ", cleaned)
    return cleaned.upper() if upper else cleaned.lower()

def count_words(text: str) -> CounterT[str]:
    """Return Counter mapping each word to its frequency."""
    return Counter(text.split())


def write_report(counts: CounterT[str], dest: Path) -> None:
    """Write the counts in 'word<space><space>count' format, alphabetically sorted."""
    max_len = max(map(len, counts)) if counts else 0
    with dest.open("w", encoding="utf-8") as fh:
        for word in sorted(counts):
            fh.write(f"{word.ljust(max_len + 2)}{counts[word]}\n")

def run(input_file: Path) -> Path:
    """High-level task coordinator. Returns the path of the report file."""
    text = read_sequence_file(input_file)
    counts = count_words(text)
    out_path = input_file.with_stem(f"{input_file.stem}_counted")
    write_report(counts, out_path)
    return out_path

def _parse_cli(argv: List[str]) -> Path:
    if len(argv) != 2:
        prog = Path(argv[0]).name
        sys.exit(f"Usage: {prog} <input_file>")
    p = Path(argv[1])
    if not p.is_file():
        sys.exit(f"ERROR: {p} not found.")
    return p

def main() -> None:
    input_path = _parse_cli(sys.argv)
    report = run(input_path)
    print(f"Done! Report written to {report}")

if __name__ == "__main__":
    main()
