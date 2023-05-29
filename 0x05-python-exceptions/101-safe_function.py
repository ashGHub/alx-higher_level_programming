#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    result = None
    try:
        result = fct(*args)
    except Exception as exp:
        sys.stderr.write(f"Exception: {exp}\n")
    return result
