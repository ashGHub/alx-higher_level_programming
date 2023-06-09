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

        Args:
            value (int): new value to set

        Raises:
            TypeError: if value is not integer
            ValueError: if value is less than zero
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

        Args:
            value (int): new value to set

        Raises:
            TypeError: if value is not integer
            ValueError: if value is less than zero
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

        Args:
            value (int): new value to set

        Raises:
            TypeError: if value is not integer
            ValueError: if value is less than zero
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

        Args:
            value (int): new value to set

        Raises:
            TypeError: if value is not integer
            ValueError: if value is less than zero
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

    def update(self, *args, **kwargs):
        """
        update rectangle attributes in one go
            1st id, 2sec width, 3rd height, 4th height
            5th x, 6th y

        Args:
            args (*args): list of arguments
            kwargs (dict): arguments in dictionary
        """
        for i in range(len(args)):
            if i == 0:
                self.id = args[0]
            elif i == 1:
                self.width = args[1]
            elif i == 2:
                self.height = args[2]
            elif i == 3:
                self.x = args[3]
            elif i == 4:
                self.y = args[4]
        if len(args) != 0:
            return
        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_dictionary(self):
        """
        returns dictionary format of this class
        """
        attrs = ["id", "width", "height", "x", "y"]
        return {attr: getattr(self, attr) for attr in attrs}

    def __str__(self):
        """
        prints string representation of rectangle class
        """
        class_name = self.__class__.__name__
        xy = f"{self.x}/{self.y}"
        wh = f"{self.width}/{self.height}"
        return f"[{class_name}] ({self.id}) {xy} - {wh}"
