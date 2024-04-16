#!/usr/bin/python3
"""A module containing script that reads stdin line by line."""


import sys

def print_metrics(total_size, status_counts):
    """Print the computed metrics."""
    print("Total file size:", total_size)
    for status_code in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")

def main():
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    try:
        for i, line in enumerate(sys.stdin, 1):
            parts = line.split()
            if len(parts) >= 5:
                status_code = int(parts[-2])
                file_size = int(parts[-1])
                total_size += file_size
                if status_code in status_counts:
                    status_counts[status_code] += 1

            if i % 10 == 0:
                print_metrics(total_size, status_counts)
    except KeyboardInterrupt:
        print_metrics(total_size, status_counts)
        sys.exit(0)

if __name__ == "__main__":
    main()
