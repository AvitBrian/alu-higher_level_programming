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

    @classmethod
    def save_to_file(cls, list_objs):
        """ saves json to file """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [i.to_dictionary() for i in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """ from load json into a string """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ creates new objects """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """ loads objects from file """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                obj = jsonfile.read()
                list_dicts = Base.from_json_string(obj)
                return [cls.create(**dictionary) for dictionary in list_dicts]
        except IOError:
            return []
