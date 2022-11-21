#!/usr/bin/python3
""" defines a class student to json"""


class Student:
    """ has student attributes """
    def __init__(self, first_name, last_name, age):
        """ initialization function """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        """return filtered dict representation of Student"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
