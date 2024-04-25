#!/usr/bin/python3
"""Contains the base class 'Base' """
import json


class Base:
    """This is class 'Base'"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) <= 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            json_string = cls.to_json_string([obj.to_dictionary()
                                             for obj in list_objs])
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json string"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)
