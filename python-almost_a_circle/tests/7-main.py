#!/usr/bin/python3
""" main function test """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 10, 10, 10)
    print(r1)

    r1.update(50)
    print(r1)

    r1.update(50, 1)
    print(r1)

    r1.update(60, 1, 2)
    print(r1)

    r1.update(53, 1, 2, 3)
    print(r1)

    r1.update(52, 1, 2, 3, 4)
    print(r1)
