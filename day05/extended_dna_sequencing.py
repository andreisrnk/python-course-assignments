import re

# Ask the user for a sequence on STDIN
sequence = input("Please type in a sequence: ")
# Extract all contiguous runs of valid bases A, C, T, G
runs = re.findall(r"[ACTG]+", sequence)
# Sort runs by length (descending)
sorted_runs = sorted(runs, key=len, reverse=True)
# Output the sorted list
print(sorted_runs)
