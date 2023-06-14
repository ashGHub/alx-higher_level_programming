#!/usr/bin/python3
"""
Student module
"""


class Student:
    """
    Student class
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes Student class

        Args:
            first_name (string): first name
            last_name (string): last name
            age (int): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        returns json representation of this class
        """
        js = self.__dict__
        if (attrs is None):
            return js
        return dict(filter(lambda item: item[0] in attrs, js.items()))
