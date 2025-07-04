import sys



def parse_log_line(line: str) -> dict:
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
    # variant1
    return list(filter(lambda log: log['level'].upper() == level.upper(), logs))
    # variant2
    # return [log for log in logs if log['level'].upper() == level.upper()]   


def count_logs_by_level(logs: list) -> dict:
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
    print("-" * len(header))
    print()  

def load_logs(file_path: str) -> list:
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


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python log_analyzer.py <log_file_path> | <level>")
        sys.exit(0)

    log_file_path = sys.argv[1]
    logs = load_logs(log_file_path)
    log_stats = count_logs_by_level(logs)
    display_log_counts(log_stats)

    if not logs:
        print("No logs found or unable to read the log file.")
        sys.exit(0)

    if len(sys.argv) > 2:
        level = sys.argv[2]
        filtered_log = filter_logs_by_level(logs, level)
        if not logs:
            print(f"No logs found for level: {level}")
            sys.exit(0)
        print(f"Деталі логів для рівня '{level}':")
        for raw in filtered_log:
            print(f"{raw['date']} {raw['time']} - {raw['message']}")

