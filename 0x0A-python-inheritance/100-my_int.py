#!/usr/bin/python3
"""
Module for MyInt
"""


class MyInt(int):
    """
    MyInt class
    """

    def __eq__(self, other):
        """
        inverts the equal comparison
        """
        return not super().__eq__(other)

    def __ne__(self, other):
        """
        inverts the not equal comparison
        """
        return not super().__ne__(other)
