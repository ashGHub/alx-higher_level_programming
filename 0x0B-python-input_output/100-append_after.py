#!/usr/bin/python3
"""
Append after module
"""


def append_after(filename="", search_string="", new_string=""):
    """
    appends a new text content after a given search key

    Args:
        filename (string): file path
        search_string (string): search key
        new_string (string): new string content
    """
    content = ""
    with open(filename, mode="r", encoding="UTF-8") as f:
        for line in f:
            content += line
            if search_string in line:
                content += new_string
    with open(filename, mode="w", encoding="UTF-8") as fw:
        fw.write(content)
