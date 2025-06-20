import sys
from pathlib import Path
from digit_utils import read_text_file, count_digits, write_digit_report

def main():
    if len(sys.argv) != 2:
        prog = Path(sys.argv[0]).name
        sys.exit(f"Usage: {prog} <INPUT_FILE>")

    src = Path(sys.argv[1])
    if not src.is_file():
        sys.exit(f"Error: '{src}' is not a regular file")

    text = read_text_file(src)
    digit_counts = count_digits(text)
    write_digit_report(digit_counts)

    print("✓ Digit counts written to report.txt")

if __name__ == "__main__":
    main()
