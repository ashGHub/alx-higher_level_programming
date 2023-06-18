#!/usr/bin/python3
"""
Module for Base class
"""


class Base:
    """
    This is a base class

    Attributes:
        __nb_objects (int): holds number of objects with out id
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        initializes the base class

        Args:
            id (int): id for the base class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
