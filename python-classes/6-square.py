#!/usr/bin/python3


class Square:


    def __init__(self, size=0, position=(0, 0):
        self.__size = size
        self.position = position


    @property
    def position(self):
        return self.position
    

    @position.setter
    def position(self, value):
        if(not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(_, int) for _ in value) or
                not all(_ >= 0 for _in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value


    @property
    def size(self):
        return self.__size


    @size.setter
    def size(self, value):
        if not value isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value


    def area(self):
        return (self.__size ** 2)


    def my_print(self):
        square_area = area()
        for _ in range(0, square_area):
            [print("#", end="") for _ in range(0, square_area)
                    print()
        if square_area == 0:
            print()
