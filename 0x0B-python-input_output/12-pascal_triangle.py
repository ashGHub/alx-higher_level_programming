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
    result = []
    if n <= 0:
        return result
    for row in range(n):
        value = []
        if (row == 0):
            value.append(1)
            result.append(value)
        elif row == 1:
            value.append(1)
            value.append(1)
            result.append(value)
        else:
            prv = result[row - 1]
            value.append(1)
            for i in range(1, row - 1):
                value.append(prv[i - 1] + prv[i])
            value.append(1)
            result.append(value)
    return result
