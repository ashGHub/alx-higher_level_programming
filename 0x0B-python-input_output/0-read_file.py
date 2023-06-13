#!/usr/bin/python3
"""
Read file module
"""


def read_file(filename=""):
    """
    reads file from a given file name

    Args:
        filename (string): path to a file
    """
    with open(filename, encoding='UTF-8') as f:
        print(f.read(), end='')
