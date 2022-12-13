#!/usr/bin/python3
""" the class Base """
import json
import csv
import turtle


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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ save to csv file """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]

                w = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    w.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ loads from csv file """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in i.items())
                              for i in list_dicts]
                return [cls.create(**i) for i in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ draws the rectangles and squares in list """
        t = turtle.Turtle()
        t.screen.bgcolor("#b7312c")
        t.pensize(5)
        t.shape("turtle")

        t.color("#ff0000")
        for r in list_rectangles:
            t.showturtle()
            t.up()
            t.goto(r.x, r.y)
            t.down()
            for _ in range(2):
                t.forward(r.width)
                t.left(90)
                t.forward(r.height)
                t.left(90)
            t.hideturtle()

        t.color("#26ff00")
        for s in list_squares:
            t.showturtle()
            t.up()
            t.goto(s.x, x.y)
            t.down()
            for _ in range(2):
                t.forward(s.width)
                t.left(90)
                t.forward(s.height)
                t.left(90)
            t.hideturtle()

        turtle.exitonclick()
