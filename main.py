import argparse
from datetime import datetime

from analyzer.parser import parse_log_line
from analyzer.date_filter import is_within_date_range
from analyzer.stats import calculate_stats
from analyzer.report import print_report

def parse_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d")

def main():
    parser = argparse.ArgumentParser(description="Python Log File Analyzer")
    parser.add_argument("logfile", help="Path to log file")
    parser.add_argument("--start-date", help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end-date", help="End date (YYYY-MM-DD)")

    args = parser.parse_args()

    start_date = parse_date(args.start_date) if args.start_date else None
    end_date = parse_date(args.end_date) if args.end_date else None

    log_entries = []

    with open(args.logfile, "r") as file:
        for line in file:
            parsed = parse_log_line(line)
            if not parsed:
                continue

            timestamp, level, message = parsed

            if is_within_date_range(timestamp, start_date, end_date):
                log_entries.append(parsed)

    stats = calculate_stats(log_entries)
    print_report(stats, len(log_entries))

if __name__ == "__main__":
    main()
