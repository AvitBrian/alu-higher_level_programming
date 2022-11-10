#!/usr/bin/python3
"""defining the class square"""


class Square:
    """ Square class definition"""

    def __init__(self, size=0):
        """ constructor initialization """

        self.__size = size

    @property
    def size(self):
        return self.size


    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

        
    def area(self):
        """Return the area of the square"""
        
        return (self.__size * self.__size)
