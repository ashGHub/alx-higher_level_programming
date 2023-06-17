#!/usr/bin/python3
"""
Module that check is kind of class
"""


def is_kind_of_class(obj, a_class):
    """
    is kind of class function
    """
    return isinstance(obj, a_class) or issubclass(type(obj), a_class)
