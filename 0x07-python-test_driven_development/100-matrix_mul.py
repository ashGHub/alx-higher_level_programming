#!/usr/bin/python3
"""
Matrix mul module
"""


def matrix_mul(m_a, m_b):
    """
    calculates matrix product of two matrices

    Args:
        m_a: list of list of integers
        m_b: list of list of integers
    """
    if (not isinstance(m_a, list)):
        raise TypeError("m_a must be a list")
    if (not isinstance(m_b, list)):
        raise TypeError("m_b must be a list")
    if (not is_list_of_lists(m_a)):
        raise TypeError("m_a must be a list of lists")
    if (not is_list_of_lists(m_b)):
        raise TypeError("m_b must be a list of lists")
    if (m_a == [[]]):
        raise ValueError("m_a can't be empty")
    if (m_b == [[]]):
        raise ValueError("m_b can't be empty")
    if (not is_int_or_float_matrix(m_a)):
        raise TypeError("m_a should contain only integers or floats")
    if (not is_int_or_float_matrix(m_b)):
        raise TypeError("m_b should contain only integers or floats")
    if (not has_same_row_size(m_a)):
        raise TypeError("each row of m_a must be of the same size")
    if (not has_same_row_size(m_b)):
        raise TypeError("each row of m_b must be of the same size")
    if (not can_be_multiplied(m_a, m_b)):
        raise ValueError("m_a and m_b can't be multiplied")
    return matrix_prod(m_a, m_b)


def is_list_of_lists(obj):
    """
    checks if object is list of lists
    """
    return all(isinstance(el, list) for el in obj)


def is_int_or_float_matrix(obj):
    """
    checks if object is list of lists of integer or float
    """
    return all(is_int_or_float(n) for el in obj for n in el)


def is_int_or_float(n):
    """
    checks if n is integer or float
    """
    return type(n) in [int, float]


def has_same_row_size(obj):
    """
    checks if obj matrix of the same row size
    """
    size = len(obj[0])
    return all(len(el) == size for el in obj)


def can_be_multiplied(m_a, m_b):
    """
    checks if the two matrix can be multiplied
    """
    a_col = len(m_a[0])
    b_row = len(m_b)
    return a_col == b_row


def matrix_prod(m_a, m_b):
    """
    returns the product of the two matrix
    """
    result = []
    for i in range(len(m_a)):
        pl = []
        for j in range(len(m_b[0])):
            p = 0
            for k in range(len(m_b)):
                p += m_a[i][k] * m_b[k][j]
            pl.append(p)
        result.append(pl)
    return result
