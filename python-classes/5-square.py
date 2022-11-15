#!/usr/bin/python3
"""Defining the class Square"""


class Square:
    """Class definition. """

    def __init__(self, size):
        """constructor initialization."""
        self.size = size

    @property
    def size(self):
        """getting the size of the square """

        return (self.__size)

    @size.setter
    def size(self, value):
        """setting the size of the square"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return calculated area of the square. """

        return (self.__size)

    def my_print(self):
        s = Square(self.__size)
        square_area = s.area()
        """print the square with the "#" character. """
        for _ in range(0, square_area):
            for _ in range(square_area):
                print("#", end="")
            print("")
        if square_area == 0:
            print("")
