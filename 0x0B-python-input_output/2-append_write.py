#!/usr/bin/python3
"""
Append file module
"""


def append_write(filename="", text=""):
    """
    append a text to given file

    Args:
        filename (string): file path
        text (string): file content
    """
    with open(filename, mode='a', encoding='UTF-8') as f:
        return f.write(text)
