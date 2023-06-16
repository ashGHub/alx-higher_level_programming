#!/usr/bin/python3
"""
Print square module
"""


def print_square(size):
    """
    prints a square with hashtag for a given size

    Args:
        size (int):  size of a square
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print(f"{'#' * size}\n" * size, end='')
