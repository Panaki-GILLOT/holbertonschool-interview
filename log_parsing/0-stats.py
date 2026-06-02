#!/usr/bin/python3
"""
Log parsing module.

Reads stdin line by line and computes metrics:
- total file size
- number of lines by status code
"""
import sys


def print_stats(total_size, status_counts):
    """Print accumulated metrics"""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


def main():
    total_size = 0
    status_counts = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0,
    }

    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()

            # Validate format
            try:
                status = parts[-2]
                size = int(parts[-1])
            except Exception:
                continue

            if status in status_counts:
                status_counts[status] += 1

            total_size += size
            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise


if __name__ == "__main__":
    main()
