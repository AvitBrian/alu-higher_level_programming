#!/usr/bin/python3
"""define a class square"""


class Square:
    """ Representing the square"""

    def __init__(self, size=0):
        """ constructor initialization and sise definition"""
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("Size must be >=0")
        self.__size = size

    def area(self):
        """ returning calculated area of the square"""
        return (self.__size ** 2)
