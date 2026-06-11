#!/usr/bin/python3
"""
Log parsing module.
"""

import sys
import re

LINE_PATTERN = re.compile(
    r'^\d+\.\d+\.\d+\.\d+ - \[.+\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$'
)

VALID_CODES = {"200", "301", "400", "401", "403", "404", "405", "500"}


def print_stats(total_size, status_counts):
    """Print accumulated metrics"""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


def main():
    total_size = 0
    status_counts = {code: 0 for code in VALID_CODES}
    line_count = 0

    try:
        for line in sys.stdin:
            match = LINE_PATTERN.match(line.rstrip('\n'))
            if not match:
                continue

            status, size = match.group(1), int(match.group(2))

            if status in status_counts:
                status_counts[status] += 1

            total_size += size
            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise

    if line_count % 10 != 0:
        print_stats(total_size, status_counts)


if __name__ == "__main__":
    main()
