#!/usr/bin/python3
"""
Add integer module
"""


def add_integer(a, b=98):
    """
    Adds two integer

    Args:
        a (int, float): first parameter
        b (int, float, optional): second parameter. Defaults to 98

    Raises:
        TypeError: a and b must be an integer

    Returns:
        int: sum of the given numbers
    """
    allowed_ts = [int, float]
    if (type(a) not in allowed_ts):
        raise TypeError("a must be an integer")
    if (type(b) not in allowed_ts):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
