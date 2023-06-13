#!/usr/bin/python3
"""
From json string module
"""


import json


def from_json_string(my_str):
    """
    returns an object from a json string

    Args:
        my_str (string): object string
    """
    return json.loads(my_str)
