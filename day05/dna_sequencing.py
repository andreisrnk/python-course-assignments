import sys
import re

if len(sys.argv) != 2:
    print(f"ERROR: {sys.argv[0]}")
    sys.exit(1)

sequence = sys.argv[1]
# return the sequences containing only ACTG
runs = re.findall(r"[ACTG]+", sequence)
print(f"the sequences containing only ACTG:  {runs}")
# sort runs by length (descending) and output
sorted_runs = sorted(runs, key=len, reverse=True)
print(sorted_runs)


