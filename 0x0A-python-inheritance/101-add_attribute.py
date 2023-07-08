#!/usr/bin/python3

""""
Module for add attribute
"""


def add_attribute(obj, att_n, att_v):
    """
    adds attributes with its value to given option

    Args:
        obj (any): object to add an attribute to
        att_n (str): attribute name
        att_v (any): attribute value
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att_n, att_v)
