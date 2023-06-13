#!/usr/bin/python3
"""
Add item module
"""


if __name__ == "__main__":
    import sys
    import json
    save_as_json = __import__("5-save_to_json_file").save_to_json_file
    load_json = __import__("6-load_from_json_file").load_from_json_file
    filename = "add_item.json"
    args = []
    if len(sys.argv) != 1:
        args = list(sys.argv[1:])
    try:
        f = load_json(filename)
    except FileNotFoundError:
        f = []
    f.extend(args)
    save_as_json(f, filename)
