#!/usr/bin/python3
"""Defining a rectangle"""


class Rectangle:
    """defining the class"""
    def __init__(self, width=0, height=0):
    """ constructor initialization"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ getting the width of the rectangle"""
        self.__width = width

    @width.setter
    def width(self, value):
        """setting the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("with must be an integer")
        elif width < 0:
            raise ValueError("with must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getting the height of the rectangle"""
        self.__height = height

    @height.setter
    def height(self, value):
        """setting the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif width < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

