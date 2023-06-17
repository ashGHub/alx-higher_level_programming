#!/usr/bin/python3
"""
Module to check if object is instance of given instance
"""


def is_same_class(obj, a_class):
    """
    check is  given is instance of given instance

    Args:
        obj (:obj"): any object type
        a_class: class to test agains to
    """
    return type(obj) == a_class
