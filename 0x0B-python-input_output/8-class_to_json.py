#!/usr/bin/python3
"""
Class to json module
"""


def class_to_json(obj):
    """
    class to json

    Args:
        obj (:obj:): object
    """
    return obj.__dict__
