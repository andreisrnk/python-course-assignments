import sys
from pathlib import Path

prog = Path(sys.argv[0]).name
if not 2 <= len(sys.argv) <= 3:
    sys.exit(f"Usage: {prog} <COLORS_FILE> [<CHOICE_NUMBER_OR_NAME>]")

colors_file = Path(sys.argv[1])
if not colors_file.is_file():
    sys.exit(f"Error: Colors file '{colors_file}' not found.")

colors = []
with colors_file.open(encoding="utf-8") as fh:
    for line in fh:
        line = line.strip()
        if line:
            colors.append(line)

print("Available colors:")
for i, color in enumerate(colors, start=1):
    print(f"  {i}. {color}")

selection = None
if len(sys.argv) == 3:
    arg = sys.argv[2]
    try:
        idx = int(arg)
        if 1 <= idx <= len(colors):
            selection = colors[idx - 1]
        else:
            sys.exit(f"Error: Selection number {idx} is out of range (1–{len(colors)}).")
    except ValueError:
        for c in colors:
            if c.lower() == arg.lower():
                selection = c
                break
        if selection is None:
            sys.exit(f"Error: '{arg}' is not a valid number or color name.")
else:
    while True:
        choice = input("Enter the number or name of your choice: ").strip()
        try:
            idx = int(choice)
            if 1 <= idx <= len(colors):
                selection = colors[idx - 1]
                break
            else:
                print(f"Please enter a number between 1 and {len(colors)}.")
                continue
        except ValueError:
            for c in colors:
                if c.lower() == choice.lower():
                    selection = c
                    break
            if selection:
                break
            else:
                print(f"'{choice}' is not a valid number or color name.")
                continue

print(f"Nice choice! '{selection}' is selected.")
