#!/usr/bin/python3
import sys


def is_safe(queens, row, col):
    for r, c in enumerate(queens):
        if c == col or abs(r - row) == abs(c - col):
            return False
    return True


def solve(n, row, queens, solutions):
    if row == n:
        solutions.append([[r, c] for r, c in enumerate(queens)])
        return
    for col in range(n):
        if is_safe(queens, row, col):
            queens.append(col)
            solve(n, row + 1, queens, solutions)
            queens.pop()


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)

solutions = []
solve(n, 0, [], solutions)
for s in solutions:
    print(s)
