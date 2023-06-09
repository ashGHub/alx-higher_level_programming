#!/usr/bin/python3
"""
Module for Base class
"""

import json
import random
import turtle


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

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        draws rectangles and squares

        Args:
            list_rectangles: list of rectangles
            list_squares: list of squares
        """
        lst = list_rectangles + list_squares
        crs = ['#FF7F50', '#FFC0CB', '#FFA500', '#FF1493', '#FF4500']
        # start draw screen at the center 
        screen = turtle.Screen()
        screen_width = screen.window_width()
        screen_height = screen.window_height()
        start_x = (screen_width // 2) - (800 // 2)
        start_y = (screen_height // 2) - (600 // 2)
        screen.setup(width=800, height=600, startx=start_x, starty=start_y)

        t = turtle.Turtle()
        for obj in lst:
            t.penup()
            t.goto(obj.x, obj.y)
            t.fillcolor(random.choice(crs))
            t.pendown()
            t.begin_fill()
            for _ in range(2):
                t.forward(obj.width)
                t.left(90)
                t.forward(obj.height)
                t.left(90)
            t.end_fill()
        turtle.done()

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

    @classmethod
    def load_from_file(cls):
        """
        returns list of instances from file
        """
        file_name = f"{cls.__name__}.json"
        with open(file_name, mode="r", encoding="UTF-8") as f:
            f_content = f.read()
            if f.tell() == 0:
                return []
            lst = Base.from_json_string(f_content)
            return [cls.create(**dct) for dct in lst]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        save CSV string representation of list_objs to a file

        Args:
            list_objs: list of base classes
        """
        file_name = f"{cls.__name__}.csv"
        with open(file_name, mode="a+", encoding="UTF-8") as f:
            if list_objs is None:
                return
            for obj in list_objs:
                dct = obj.to_dictionary()
                is_square = dct.get('size', -1) != -1
                s = ""
                if is_square:
                    s = dct['size']
                else:
                    s = f"{dct['width']},{dct['height']}"
                data = f"{dct['id']},{s},{dct['x']},{dct['y']}\n"
                f.write(data)

    @classmethod
    def load_from_file_csv(cls):
        """
        returns list of instances from file
        """
        file_name = f"{cls.__name__}.csv"
        result = []
        with open(file_name, mode="r", encoding="UTF-8") as f:
            for line in f:
                lst_r = line.split(",")
                lst = [int(x) for x in lst_r]
                d = {}
                is_square = len(lst) == 4
                if is_square:
                    d["id"], d["size"], d["x"], d["y"] = lst
                else:
                    d["id"], d["width"], d["height"], d["x"], d["y"] = lst
                result.append(cls.create(**d))
        return result
