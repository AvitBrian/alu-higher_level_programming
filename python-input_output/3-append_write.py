#!/usr/bin/python3
"""function that adds a string at the EOF"""


def append_write(filename="", text=""):
    """appends a string to the end of file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
