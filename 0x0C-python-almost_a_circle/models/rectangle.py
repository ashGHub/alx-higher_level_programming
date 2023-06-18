#!/usr/bin/python3
"""
Module for rectangle
"""

from .base import Base


class Rectangle(Base):
    """
    Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initializes rectangle class

        Args:
            width (int): width for rectangle
            height (int): height for rectangle
            x (int): x coordinate
            y (int): y coordinate
            id (int): id to pass to base class
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter for width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        getter for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter for height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        getter for x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        setter for x
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        getter for y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        setter for y
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        calculates and returns the area of this rectangle
        """
        return self.width * self.height

    def display(self):
        """
        prints the rectiangle area using symbols
        """
        print(" \n" * self.y, end='')
        print(f"{' ' * self.x}{'#' * self.width}\n" * self.height, end='')

    def __str__(self):
        """
        prints string representation of rectangle class
        """
        xy = f"{self.x}/{self.y}"
        wh = f"{self.width}/{self.height}"
        return f"[Rectangle] ({self.id}) {xy} - {wh}"
