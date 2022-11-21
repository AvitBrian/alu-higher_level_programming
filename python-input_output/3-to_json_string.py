#!/usr/bin/python3
""" defines a function that returns a json string rep"""
import json


def to_json_string(my_obj):
    """returns json representation of an object"""
    return json.dumps(my_obj)
