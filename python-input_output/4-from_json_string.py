#!/usr/bin/python3
"""returns a string from a json"""
import json


def from_json_string(my_str):
    """ return the python object rep of a json string"""
    return json.loads(my_str)
