#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics."""

import sys


def print_metrics(size, status_codes):
    """Print accumulated metrics.
    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_metrics(size, status_codes)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                size += int(line[-1])  # Accumulate file size
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if line[-2] not in status_codes:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass

        print_metrics(size, status_codes)

    except KeyboardInterrupt:
        print_metrics(size, status_codes)
        raise
