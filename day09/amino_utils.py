from collections import Counter
import re

# Codon to amino acid table
CODON_TABLE = {
    'Phe': ['TTT', 'TTC'], 'Leu': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
    'Ile': ['ATT', 'ATC', 'ATA'], 'Met': ['ATG'], 'Val': ['GTT', 'GTC', 'GTA', 'GTG'],
    'Ser': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'], 'Pro': ['CCT', 'CCC', 'CCA', 'CCG'],
    'Thr': ['ACT', 'ACC', 'ACA', 'ACG'], 'Ala': ['GCT', 'GCC', 'GCA', 'GCG'],
    'Tyr': ['TAT', 'TAC'], 'His': ['CAT', 'CAC'], 'Gln': ['CAA', 'CAG'],
    'Asn': ['AAT', 'AAC'], 'Lys': ['AAA', 'AAG'], 'Asp': ['GAT', 'GAC'],
    'Glu': ['GAA', 'GAG'], 'Cys': ['TGT', 'TGC'], 'Trp': ['TGG'],
    'Arg': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'], 'Gly': ['GGT', 'GGC', 'GGA', 'GGG'],
    'STOP': ['TAA', 'TAG', 'TGA']
}

# Codon to amino acid lookup (flattened)
CODON_LOOKUP = {codon: aa for aa, codons in CODON_TABLE.items() for codon in codons}


def clean_sequence(raw_text):
    """
    Remove FASTA headers and non-ACGT characters from DNA string.

    >>> clean_sequence('''>header
    ... ATGCNNN
    ... GGG''')
    'ATGCGGG'
    """
    lines = raw_text.splitlines()
    cleaned = "".join(line.strip() for line in lines if not line.startswith(">"))
    return re.sub(r"[^ACGT]", "", cleaned.upper())


def count_amino_acids(seq):
    """
    Count amino acids from a DNA sequence in reading frame 0.

    >>> count_amino_acids("ATGTTT")
    Counter({'Met': 1, 'Phe': 1})
    >>> count_amino_acids("ATGTTTAAA")
    Counter({'Met': 1, 'Phe': 1, 'Lys': 1})
    """
    counts = Counter()
    for i in range(0, len(seq) - 2, 3):
        codon = seq[i:i+3]
        aa = CODON_LOOKUP.get(codon)
        if aa:
            counts[aa] += 1
    return counts


def format_counts(counts):
    """
    Format amino acid counts into a list of strings.

    >>> format_counts(Counter({'Met': 2, 'Gly': 1}))[:3]
    ['Ala   0', 'Arg   0', 'Asn   0']
    """
    max_len = max(len(aa) for aa in CODON_TABLE)
    return [f"{aa.ljust(max_len + 2)}{counts.get(aa, 0)}" for aa in sorted(CODON_TABLE)]
