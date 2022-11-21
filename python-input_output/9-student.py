#!/usr/bin/python3
""" defines a class student to json"""


class Student:
    """ has student attributes """
    def __init__(self, first_name, last_name, age):
        """ initialization function """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ return dict representation of Student"""
        return self.__dict__
