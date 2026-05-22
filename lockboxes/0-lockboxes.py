#!/usr/bin/python3
"""Module for checking if all boxes can be unlocked."""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
        boxes (list): A list of lists containing keys.

    Returns:
        bool: True if all boxes can be opened, otherwise False.
    """
    opened = [0]
    keys = [0]

    while keys:
        current_box = keys.pop()

        for key in boxes[current_box]:
            if key not in opened and key < len(boxes):
                opened.append(key)
                keys.append(key)

    return len(opened) == len(boxes)
