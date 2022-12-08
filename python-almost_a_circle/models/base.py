#!/usr/bin/python3
""" the class Base """

class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ init function"""    
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
