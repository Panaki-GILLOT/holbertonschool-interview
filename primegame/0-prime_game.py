#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    """
    Determines the winner of the prime game.

    Args:
        x (int): Number of rounds.
        nums (list): List of n values for each round.

    Returns:
        str: "Maria" if Maria wins the most rounds,
             "Ben" if Ben wins the most rounds,
             None if there is a tie or invalid input.
    """
    if not nums or x < 1:
        return None

    max_n = max(nums)

    # Sieve of Eratosthenes
    sieve = [True] * (max_n + 1)
    if max_n >= 0:
        sieve[0] = False
    if max_n >= 1:
        sieve[1] = False

    p = 2
    while p * p <= max_n:
        if sieve[p]:
            multiple = p * p
            while multiple <= max_n:
                sieve[multiple] = False
                multiple += p
        p += 1

    # prime_count[i] = number of primes <= i
    prime_count = [0] * (max_n + 1)
    count = 0
    for i in range(max_n + 1):
        if sieve[i]:
            count += 1
        prime_count[i] = count

    maria = 0
    ben = 0

    for i in range(min(x, len(nums))):
        if prime_count[nums[i]] % 2 == 1:
            maria += 1
        else:
            ben += 1

    if maria > ben:
        return "Maria"
    if ben > maria:
        return "Ben"
    return None