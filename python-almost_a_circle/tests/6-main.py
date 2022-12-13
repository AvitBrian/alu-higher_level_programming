#!/usr/bin/python3
""" main function test """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(3, 4, 3, 1)
    r1.display()

    print("---")

    r2 = Rectangle(9, 3, 2, 1)
    r2.display()
