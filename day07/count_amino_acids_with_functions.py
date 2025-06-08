from __future__ import annotations
from collections import Counter
from pathlib import Path
from typing import Dict, List
import re
import sys

CODON_TABLE: Dict[str, List[str]] = {
    'Phe': ['TTT', 'TTC'],
    'Leu': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
    'Ile': ['ATT', 'ATC', 'ATA'],
    'Met': ['ATG'],
    'Val': ['GTT', 'GTC', 'GTA', 'GTG'],
    'Ser': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
    'Pro': ['CCT', 'CCC', 'CCA', 'CCG'],
    'Thr': ['ACT', 'ACC', 'ACA', 'ACG'],
    'Ala': ['GCT', 'GCC', 'GCA', 'GCG'],
    'Tyr': ['TAT', 'TAC'],
    'His': ['CAT', 'CAC'],
    'Gln': ['CAA', 'CAG'],
    'Asn': ['AAT', 'AAC'],
    'Lys': ['AAA', 'AAG'],
    'Asp': ['GAT', 'GAC'],
    'Glu': ['GAA', 'GAG'],
    'Cys': ['TGT', 'TGC'],
    'Trp': ['TGG'],
    'Arg': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'Gly': ['GGT', 'GGC', 'GGA', 'GGG'],
    'STOP': ['TAA', 'TAG', 'TGA'],
}

CODON_LOOKUP: Dict[str, str] = {
    codon: aa for aa, codons in CODON_TABLE.items() for codon in codons
}


def clean_sequence(raw: str) -> str:
    """Return uppercase string of ACTG only (headers / whitespace removed)."""
    # Strip FASTA headers then non-ACTG chars
    no_headers = "\n".join(
        line for line in raw.splitlines() if not line.startswith(">")
    )
    return re.sub(r"[^ACGTacgt]", "", no_headers).upper()


def translate(seq: str, frame: int = 0) -> Counter:
    if frame not in (0, 1, 2):
        raise ValueError("frame must be 0, 1 or 2")

    counts: Counter[str] = Counter()
    for i in range(frame, len(seq) - 2, 3):
        codon = seq[i : i + 3]
        aa = CODON_LOOKUP.get(codon)
        if aa:
            counts[aa] += 1
    return counts

def read_file(path: Path) -> str:
    """Read text from *path* (UTF-8)."""
    return path.read_text(encoding="utf-8")


def write_report(counts: Counter, out_path: Path) -> None:
    """Write an alphabetically-sorted count table to *out_path*."""
    max_len = max(map(len, CODON_TABLE))
    with out_path.open("w", encoding="utf-8") as fh:
        for aa in sorted(CODON_TABLE):
            fh.write(f"{aa.ljust(max_len + 2)}{counts.get(aa, 0)}\n")

def run(input_file: Path, frame: int = 0) -> Path:
    raw = read_file(input_file)
    seq = clean_sequence(raw)
    counts = translate(seq, frame=frame)
    out_path = input_file.with_stem(f"{input_file.stem}_aa_count")
    write_report(counts, out_path)
    return out_path

def _parse_cli(argv: List[str]) -> tuple[Path, int]:
    if not (2 <= len(argv) <= 3):
        prog = Path(argv[0]).name
        sys.exit(f"Usage: {prog} <dna_file> [frame 0|1|2]")
    file_path = Path(argv[1])
    if not file_path.is_file():
        sys.exit(f"ERROR: {file_path} not found.")
    frame = int(argv[2]) if len(argv) == 3 else 0
    if frame not in (0, 1, 2):
        sys.exit("Reading frame must be 0, 1 or 2.")
    return file_path, frame


def main() -> None:
    infile, frame = _parse_cli(sys.argv)
    report = run(infile, frame)
    print(f"Done! Amino-acid counts written to {report}")


if __name__ == "__main__":
    main()
