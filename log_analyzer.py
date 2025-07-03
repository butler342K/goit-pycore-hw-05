import sys



def parse_log_line(line: str) -> dict:
    """
    Parse a single line of the log file and return a dictionary with the parsed data.
    """
    parts = line.strip().split()
    if len(parts) < 3:
        return None
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': ' '.join(parts[3:])
    }
def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['level'].lower() == level.lower()]

def count_logs_by_level(logs: list) -> dict:
    """
    Count the number of log entries for each log level.
    Returns a dictionary with log levels as keys and counts as values.
    """
    level_count = {}
    for log in logs:
        level = log['level']
        if level in level_count:
            level_count[level] += 1
        else:
            level_count[level] = 1
    return level_count

def display_log_counts(counts: dict):
    header = "Рівень логування | Кількість"
    header_field1 = "Рівень логування"
    header_field2 = "Кількість"
    header = header_field1 + " | " + header_field2
    print(header)
    print("-" * len(header))
    for level, count in counts.items():
        print(f"{level:<{len(header_field1)}} |{count:^{len(header_field2)}}")
    print()  # Add a newline for better readability

def load_logs(file_path: str) -> list:
    """
    Load the log file and return a list of dictionaries with parsed log entries.
    """
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parsed_line = parse_log_line(line)
                if parsed_line:
                    logs.append(parsed_line)
    except FileNotFoundError:
        print(f"Log file {file_path} not found.")
    return logs

def main():
    if __name__ == "__main__":
        if len(sys.argv) != 2:
            print("Usage: python log_analyzer.py <log_file_path>")
            sys.exit(0)

        log_file_path = sys.argv[1]
        logs = load_logs(log_file_path)

        if not logs:
            print("No logs found or unable to read the log file.")
            sys.exit(0)
        log_stats = count_logs_by_level(logs)
        display_log_counts(log_stats)
        # for log in logs:
            # print(f"{log['timestamp']} [{log['level']}] {log['message']}")

main()