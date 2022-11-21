#!/usr/bin/python3
"""a function that creates an object from a json file"""
import json


def load_from_json_file(filename):
    """creates a json file"""
    with open(filename) as f:
        return Json.load(f)
