celestial_objects = ['Moon', 'Gas', 'Asteroid', 'Dwarf', 'Asteroid', 'Moon', 'Asteroid']

# Use an ordered dictionary (insertion order) to count occurrences
counts = {}
for obj in celestial_objects:
    counts[obj] = counts.get(obj, 0) + 1

print(counts)
# Print each word and its count, aligned in columns
for word, cnt in counts.items():
    print(f"{word:<12}{cnt}")
