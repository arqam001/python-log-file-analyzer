
import re

def calculate_stats(log_entries):
    stats = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0,
        "response_times": []
    }

    for _, level, message in log_entries:
        if level in stats:
            stats[level] += 1

        match = re.search(r"(\d+)ms", message)
        if match:
            stats["response_times"].append(int(match.group(1)))

    return stats
