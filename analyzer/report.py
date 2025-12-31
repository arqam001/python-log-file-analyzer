
def print_report(stats, total_logs):
    print("\nLog Summary")
    print("-" * 20)
    print(f"Total logs processed: {total_logs}")
    print(f"INFO: {stats['INFO']}")
    print(f"WARNING: {stats['WARNING']}")
    print(f"ERROR: {stats['ERROR']}")

    if stats["response_times"]:
        avg = sum(stats["response_times"]) / len(stats["response_times"])
        print(f"Average response time: {avg:.2f} ms")
