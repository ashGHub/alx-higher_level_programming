#!/usr/bin/python3
"""
Write file module
"""


def write_file(filename="", text=""):
    """
    writes a text to given file

    Args:
        filename (string): file path
        text (string): new file content
    """
    with open(filename, mode='w', encoding='UTF-8') as f:
        return f.write(text)
