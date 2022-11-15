#!/usr/bin/python3

"""Square Class Representation"""


class Square:
    """ Class Square definition. """

    def __init__(self, size=0, position=(0, 0):
        """ initializing class constructor. """
        self.__size = size
        self.__position = position

    @property
    def position(self):
        """ getting position of the square. """

        return self.position

    @position.setter
    def position(self, value):
        """ setting the position of the square. """

        if(not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(_, int) for _ in value) or
                not all(_ >= 0 for _in value)):
            raise TypeError("position must be a tuple of 2 positive integers.")
        self.__position = value

    @property
    def size(self):
        """ getting the size of the square. """
        return self.__size

    @size.setter
    def size(self, value):
        """ setting the size of the square. """
        if not value isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ calculating area of the square. """

        return (self.__size)


    def my_print(self):
        """ printing the square. """
        s = Square(self.__size)
        square_area = s.area()
        for _ in range(0, square_area):
            [print("#", end="") for _ in range(0, square_area)] 
            print()
        if square_area == 0:
            print()
