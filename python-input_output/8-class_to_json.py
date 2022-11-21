#!/usr/bin/python3
""" a python class to json function """


def class_to_json(obj):
    """ return a dictionary representaion of a simple data structure """
    return obj.__dict__
