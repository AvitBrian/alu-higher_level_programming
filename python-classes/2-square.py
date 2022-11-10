#!/usr/bin/python3
""" the class square with size and size validation"""

class Square:
    """ defining the class square. """


    def __init__(self, size=0):
        """defining size and validation"""
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("Size must be >=0")
        self.__size = size
