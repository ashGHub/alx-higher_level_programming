#!/usr/bin/python3
"""
Save to json file module
"""

import json


def save_to_json_file(my_obj, filename):
    """
    saves object to json file

    Args:
        my_obj (:obj:): object to write
        filename (string): file path
    """
    with open(filename, mode='w', encoding='UTF-8') as f:
        json.dump(my_obj, f)
