#!/usr/bin/python3
"""
Module for square class
"""

from .rectangle import Rectangle


class Square(Rectangle):
    """
    square class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        initializes square class

        Args:
            size (int): on side size of square
            x (int): x coordinate
            y (int): y coordinate
            id (int): id for the rsquare
        """
        super().__init__(size, size, x,  y, id)

    def __str__(self):
        """
        prints string representation of rectangle class
        """
        class_name = self.__class__.__name__
        xy = f"{self.x}/{self.y}"
        return f"[{class_name}] ({self.id}) {xy} - {self.width}"
