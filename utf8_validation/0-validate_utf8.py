#!/usr/bin/python3
"""
Module that validates UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents
    a valid UTF-8 encoding.

    Args:
        data (list): List of integers.

    Returns:
        bool: True if valid UTF-8, otherwise False.
    """
    remaining_bytes = 0

    for num in data:
        byte = num & 0xFF

        if remaining_bytes == 0:
            if (byte >> 7) == 0:
                continue
            elif (byte >> 5) == 0b110:
                remaining_bytes = 1
            elif (byte >> 4) == 0b1110:
                remaining_bytes = 2
            elif (byte >> 3) == 0b11110:
                remaining_bytes = 3
            else:
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            remaining_bytes -= 1

    return remaining_bytes == 0