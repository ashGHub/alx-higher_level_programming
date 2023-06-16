#!/usr/bin/python3
"""
Text indentation module
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters
    . ? :

    Args:
        text (str): text to print
    """
    chrt = ['.', '?', ':']
    skip_space = False
    if type(text) != str:
        raise TypeError("text must be a string")
    for c in text.strip():
        skip_space = c == ' ' and skip_space
        if skip_space:
            continue
        if c in chrt:
            print(f"{c}\n")
            skip_space = True
        else:
            print(f"{c}", end='')
