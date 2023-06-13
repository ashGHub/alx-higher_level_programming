#!/usr/bin/python3
"""
To json string module
"""


import json


def to_json_string(my_obj):
    """
    changes an object to json string

    Args:
        my_obj (:obj:): data object
    """
    return json.dumps(my_obj)
