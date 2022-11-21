#!/usr/bin/python3
""" a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """writes from the string provided in the string arg"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
