#!/usr/bin/python3
"""
Pascal triangle module
"""


def pascal_triangle(n):
    """
    returns a list of list of integers representing Pascals's triangle

    Args:
        n: size of pascal triangle
    """
    result = [[1]]
    if n <= 0:
        return []
    for row in range(1, n):
        value = [1]
        prv = result[row - 1]
        for i in range(1, row):
            value.append(prv[i - 1] + prv[i])
        value.append(1)
        result.append(value)
    return result
