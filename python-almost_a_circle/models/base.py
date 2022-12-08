#!/usr/bin/python3
""" the class Base """
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ init function"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    def to_json_string(list_dictionaries):
        """ json dump string """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        new = json.dumps(list_dictionaries)
        return new
