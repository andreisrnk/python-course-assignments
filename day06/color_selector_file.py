import sys
from pathlib import Path

color_file = Path(sys.argv[1]) if len(sys.argv) == 2 else Path("colors.txt")
if not color_file.is_file():
    sys.exit(f"Error: '{color_file}' not found.")

with color_file.open(encoding="utf-8") as fh:
    allowed = {line.strip().lower() for line in fh if line.strip()}

while True:
    user_color = input("Pick a color: ").strip().lower()
    if user_color in allowed:
        print(f"Nice choice! '{user_color}' is in the list.")
    else:
        print(f"Sorry, '{user_color}' isn’t in the list. Goodbye!")
        break
