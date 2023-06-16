#!/usr/bin/python3
"""
Say my name module
"""


def say_my_name(first_name, last_name=""):
    """
    prints given full name

    Args:
        first_name (str): first name
        last_name (str): last name
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
