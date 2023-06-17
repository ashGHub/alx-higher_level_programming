#!/usr/bin/python3
"""
Module that checks if object inheritance
"""


def inherits_from(obj, a_class):
    """
    inherits from function
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
