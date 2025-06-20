import sys
from pathlib import Path
from amino_utils import clean_sequence, count_amino_acids, format_counts

def main(file_path):
    path = Path(file_path)
    if not path.is_file():
        sys.exit(f"ERROR: {file_path} not found.")

    seq = path.read_text(encoding="utf-8")
    cleaned_seq = clean_sequence(seq)
    if len(cleaned_seq) < 3:
        sys.exit("ERROR: sequence length < 3 bases.")

    counts = count_amino_acids(cleaned_seq)
    out_path = path.with_stem(f"{path.stem}_aa_count")

    with out_path.open("w", encoding="utf-8") as f:
        for line in format_counts(counts):
            f.write(line + "\n")

    print(f"Done! Amino-acid counts written to {out_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(f"Usage: {Path(sys.argv[0]).name} <dna_file>")
    main(sys.argv[1])
