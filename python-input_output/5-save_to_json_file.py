#!/usr/bin/python3
""" defines a function that writes to a file using json"""
import json


def save_to_json_file(my_obj, filename):
    """ write to a file using json"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
