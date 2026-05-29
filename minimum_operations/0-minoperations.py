#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    Calculate the minimum number of operations needed
    to reach exactly n H characters.

    Args:
        n (int): target number of H characters

    Returns:
        int: minimum number of operations
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
