#!/usr/bin/python3
"""
Matrix divided  module
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix

    Args:
        matrix (:obj:`list` of :obj:`list` of :obj:`int`):
            list of list of integer
        div (int): number to divide with
    """
    if not has_valid_type(matrix):
        raise_must_be_int_or_float()
    if not has_same_size(matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(x / div, 2) for x in lst] for lst in matrix]


def has_valid_type(matrix):
    """
    checks if matrix elements are all integer or float

    Returns true if all elements are integer or float, else false
    """
    allowed_t = [int, float]
    invalids = [x for lst in matrix for x in lst if type(x) not in allowed_t]
    return len(invalids) == 0


def raise_must_be_int_or_float():
    """
    raise type error
    """
    msg_1 = "matrix must be a matrix"
    msg_2 = "(list of lists) of integers/floats"
    raise TypeError(f"{msg_1} {msg_2}")


def has_same_size(matrix):
    """
    checks if matrix elements have the same size

    Args:
        matrix (:obj:`list` of :obj:`list` of :obj:`int`):
            list of list of integer

    Returns true if matrix have the same element else false
    """
    size_set = {len(i) for i in matrix}
    return len(size_set) == 1
