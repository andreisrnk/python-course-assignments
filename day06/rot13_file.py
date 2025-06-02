import sys
import codecs
from pathlib import Path

# Expect exactly one argument: the source file
if len(sys.argv) != 2:
    prog = Path(sys.argv[0]).name
    sys.exit(f"Usage: {prog} FILENAME")

file_path = Path(sys.argv[1])
if not file_path.is_file():
    sys.exit(f"Error: '{file_path}' is not a regular file")

# Read → ROT13 → write to new file
original_text = file_path.read_text(encoding="utf-8") # read the file content
rot13_text = codecs.encode(original_text, "rot_13") # apply ROT13 encoding

dst = file_path.with_suffix(file_path.suffix + ".rot13")  # creates new file with .rot13
dst.write_text(rot13_text, encoding="utf-8")

print(f"✓ ROT13 written to {dst}")
