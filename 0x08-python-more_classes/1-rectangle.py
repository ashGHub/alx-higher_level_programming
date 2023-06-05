#!/usr/bin/python3
"""
This is a rectangle module
"""


class Rectangle:
    """
    Rectangle class definition
    """

    def __init__(self, width=0, height=0):
        """
        Initialize the class object

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        Gets width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for rectangle width
        """
        if (type(value) != int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for rectangle height
        """
        if (type(value) != int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value
