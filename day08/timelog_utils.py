import re
from datetime import datetime, timedelta
from collections import defaultdict

TIME_PATTERN = re.compile(r"^(\d{2}:\d{2}) (.+)$", re.MULTILINE)

def parse_log(content):
    all_sessions = []
    for block in content.strip().split("\n\n"):
        matches = TIME_PATTERN.findall(block.strip())
        block_sessions = []
        for i in range(len(matches) - 1):
            start, label = matches[i]
            end, _ = matches[i + 1]
            block_sessions.append((start, end, label))
        all_sessions.append(block_sessions)
    return all_sessions

def write_report(all_sessions, output_path):
    with output_path.open("w", encoding="utf-8") as f:
        for block in all_sessions:
            for start, end, label in block:
                f.write(f"{start}-{end} {label}\n")
            f.write("\n")

def to_minutes(start, end):
    fmt = "%H:%M"
    t1 = datetime.strptime(start, fmt)
    t2 = datetime.strptime(end, fmt)
    diff = (t2 - t1)
    return int(diff.total_seconds() // 60)

def summarize_durations(all_sessions):
    durations = defaultdict(int)
    total_minutes = 0

    for block in all_sessions:
        for start, end, label in block:
            mins = to_minutes(start, end)
            durations[label] += mins
            total_minutes += mins

    for label in sorted(durations, key=durations.get, reverse=True):
        mins = durations[label]
        perc = round(mins / total_minutes * 100)
        print(f"{label:<25} {mins:>3} minutes   {perc}%")
