#!/usr/bin/python3
"""Defining the class Square"""


class Square:
    """Class definition. """

    def __init__(self, size, position):
        """constructor initialization."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """getting the size of the square """

        return (self.__size)
    @property
    def property(self):
        """getting the position of the square"""
        return (self.__property)

    @size.setter
    def size(self, value):
        """setting the size of the square"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) !=2 or
                not all(isinstance(_, int) for _ in value) or
                not all(_ >= 0 for _ in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value


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
            return 

        [print("") for i in range(0, self.__position[1])]
        for _ in range(0, self.__size):
            [print(" ", end="") for _ in range(0, self.__position[0])]
            [print(" ", end="") for _ in range(0, self.__size)]
            print()
