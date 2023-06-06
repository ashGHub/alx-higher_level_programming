#!/usr/bin/python3
"""
This is a rectangle module
"""


class Rectangle:
    """
    Rectangle class definition

    Attributes:
        number_of_instances (int): number of rectangle instances
        print_symbol (any): symbol used for string representation
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes the class object

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

        Args:
            value (int): integer value to set the width

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than zero
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

        Args:
            value (int): integer value to set the height

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than zero
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
        smb = str(self.print_symbol)
        return (f"{smb * self.width}\n" * self.height)[:-1]

    def __repr__(self):
        """
        Returns string format to create new rectangle instance
        """
        return f"Rectangle{self.width, self.height}"

    def __del__(self):
        """
        Called during instance destruction
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        returns the rectangle with biggest area else returns rect_1

        Args:
            rect_1 (Rectangle): first rectangle
            rect_2 (Rectangle): second rectangle

        Raises:
            TypeError: if rect_1 or rect_2 is not type of Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Creates a square from Rectangle class

        Args:
            size (int): size of the new square
        """
        return cls(size, size)
