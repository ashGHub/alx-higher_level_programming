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
        self.__y = value
