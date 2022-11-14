#!/usr/bin/python3

""" the class square calculating and displaying a square"""


class Square:
    """Class definition. """
    def __init__(self, size=0):
        """constructor initialized"""
        self.__size = size
    @property
    def size(self):
        """getting the size of the square"""
        return self.__size
    @size.setter
    def size(self, value):
        """setting the size of the square"""
        if not value isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        """Return calculated area of the square"""
        return (self.__size ** 2)
    def my_print(self):
        """print the square with the "#" character. """
        square_area = area()
        for _ in range(0, square_area):
            [print("#", end="") for _ in range(0, square_area)
                    print()
                if square_area == 0:
            print()
