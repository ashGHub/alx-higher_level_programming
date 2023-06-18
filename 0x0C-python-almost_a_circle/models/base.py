#!/usr/bin/python3
"""
Module for Base class
"""

import json


class Base:
    """
    This is a base class

    Attributes:
        __nb_objects (int): holds number of objects created
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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representaiton of list_dictionaries

        Args:
            list_dictionaries (dict): list of dictionaries to parse
        """
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of JSON string representation

        Args:
            json_string (JSON): json string to parse
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance of a class from attributes in dictionary

        Args:
            dictionary: holds all attribute values
        """
        result = cls(1, 1, 1)
        result.update(**dictionary)
        return result

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save JSON string representation of list_objs to a file

        Args:
            list_objs: list of base classes
        """
        file_name = f"{cls.__name__}.json"
        with open(file_name, mode="w+", encoding="UTF-8") as f:
            if list_objs is None:
                return
            data = []
            for obj in list_objs:
                data.append(obj.to_dictionary())
            f.write(Base.to_json_string(data))
