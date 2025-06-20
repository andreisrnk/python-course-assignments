from pathlib import Path
from timelog_utils import parse_log, write_report, summarize_durations

def main():
    input_path = Path("timelog.log")
    output_path = Path("timelog.txt")

    with input_path.open(encoding="utf-8") as f:
        content = f.read()

    all_sessions = parse_log(content)
    write_report(all_sessions, output_path)
    summarize_durations(all_sessions)

if __name__ == "__main__":
    main()
