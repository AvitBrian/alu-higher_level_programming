#!/usr/bin/python3


class Square:


    def __init__(self, size=0):
        self.__size = size

    
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
