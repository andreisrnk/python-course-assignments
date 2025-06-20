from amino_utils import clean_sequence, count_amino_acids, format_counts

def test_clean_sequence():
    raw = """>header
ATGCNNN
GGG"""
    assert clean_sequence(raw) == "ATGCGGG"

def test_count_amino_acids():
    result = count_amino_acids("ATGTTTGAA")
    assert result["Met"] == 1
    assert result["Phe"] == 1
    assert result["Glu"] == 1

def test_format_counts():
    counts = {'Met': 2, 'Gly': 1}
    lines = format_counts(counts)
    assert any("Met" in line and "2" in line for line in lines)
    assert any("Gly" in line and "1" in line for line in lines)
