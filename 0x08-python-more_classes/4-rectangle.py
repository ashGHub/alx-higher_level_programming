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
        Sets the rectangle width
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
        Sets the rectangle height
        """
        if (type(value) != int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle
        """
        return self.height * self.width

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Returns string format
        """
        if self.width == 0 or self.height == 0:
            return ""
        # -1 removes the last new line
        return (f"{'#' * self.width}\n" * self.height)[:-1]

    def __repr__(self):
        """
        Returns string format to create new rectangle instance
        """
        return f"Rectangle{self.width, self.height}"
