from pathlib import Path
from collections import Counter
import sys
import re

codon_table = {
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

# --- 1. Parse CLI argument ---------------------------------------------------
if len(sys.argv) != 2:
    print(f"Usage: {Path(sys.argv[0]).name} <dna_file>", file=sys.stderr)
    sys.exit(1)

in_path = Path(sys.argv[1])
if not in_path.is_file():
    print(f"ERROR: {in_path} not found.", file=sys.stderr)
    sys.exit(1)

# --- 2. Read & clean sequence ------------------------------------------------
seq_lines = []
with in_path.open(encoding="utf-8") as fh:
    for line in fh:
        if line.startswith(">"):        # skip FASTA headers
            continue
        seq_lines.append(line.strip())

sequence = "".join(seq_lines).upper()
sequence = re.sub(r"[^ACGT]", "", sequence)   # strip everything but ACTG

if len(sequence) < 3:
    print("ERROR: sequence length < 3 bases.", file=sys.stderr)
    sys.exit(1)

# --- 3. Build codon → amino-acid lookup dict --------------------------------
codon_lookup = {codon: aa for aa, codons in codon_table.items() for codon in codons}

# --- 4. Scan sequence, count amino acids ------------------------------------
counts = Counter()
for i in range(0, len(sequence) - 2, 3):  # reading frame 0
    codon = sequence[i:i+3]
    aa = codon_lookup.get(codon, None)
    if aa:                 # ignore unknown codons (e.g., N's in sequencing data)
        counts[aa] += 1

# --- 5. Prepare output -------------------------------------------------------
out_path = in_path.with_stem(f"{in_path.stem}_aa_count")
max_len = max(len(aa) for aa in codon_table)

with out_path.open("w", encoding="utf-8") as fh:
    for aa in sorted(codon_table):               # alphabetical
        fh.write(f"{aa.ljust(max_len + 2)}{counts.get(aa, 0)}\n")

print(f"Done! Amino-acid counts written to {out_path}")
