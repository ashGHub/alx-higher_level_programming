#!/usr/bin/python3
"""
This module contians a square definition
"""


class Square:
    """A square class
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the class with a data

        Args:
            size: size of the square
            position: x and y cooridinate position

        Attributes:
            size: size of the square
            position: x and y coorindate position

        """
        self.size = size
        self.position = position

    def area(self):
        """Calculate the are of the current square
        """
        return self.__size ** 2

    @property
    def size(self):
        """Gets the current square size
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

    @property
    def position(self):
        """Gets the current square position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the curren square position to a new value
        """
        if (type(value) != tuple
                or len(value) != 2
                or type(value[0]) != int
                or type(value[0]) != int
                or value[0] < 0
                or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value) != tuple or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints square size in hashtag
        and prints position 0 as new line and position 1 as space
        """
        if self.size == 0:
            print('')
            return
        for p in range(self.position[1]):
            print('')
        for s in range(self.size):
            print(' ' * self.position[0] + "#" * self.size)
