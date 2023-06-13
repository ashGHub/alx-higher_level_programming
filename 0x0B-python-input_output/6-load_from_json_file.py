#!/usr/bin/python3
"""
Load from json file module
"""


import json


def load_from_json_file(filename):
    """
    load from json file

    Args:
        filename (string): file path
    """
    with open(filename, encoding='UTF-8') as f:
        return json.load(f)
