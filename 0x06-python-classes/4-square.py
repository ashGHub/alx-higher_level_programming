#!/usr/bin/python3
"""
This module contians a square definition
"""


class Square:
    """A square class
    """

    def __init__(self, size=0):
        """Initialize the class with a data

        Args:
            size: size of the square

        Attributes:
            size: size of the square

        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate the are of the current square
        """
        return self.__size ** 2

    @property
    def size(self):
        """Get the current square size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the current square size to a new value
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
