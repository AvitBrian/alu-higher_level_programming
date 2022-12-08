#!/usr/bin/python3
""" the class Base """
import json
import csv


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ json dump string """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        new = json.dumps(list_dictionaries)
        return new

    def save_to_file(cls, list_objs):
        """ saves json to file """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if listobjs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [i.to_dictionary() for i in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))
