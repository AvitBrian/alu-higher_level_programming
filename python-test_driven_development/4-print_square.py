#!/usr/bin/python3
""" print square function """


def print_square(size):
    """ prints a square """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        for _ in range(size):
            print("#", end="")
        print()
