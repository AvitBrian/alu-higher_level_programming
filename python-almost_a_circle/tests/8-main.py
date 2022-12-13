#!/usr/bin/python3
""" main function test """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 10, 10, 10)
    print(r1)

    r1.update(height=2)
    print(r1)

    r1.update(width=5, x=3)
    print(r1)

    r1.update(y=1, width=5, x=1, id=50)
    print(r1)

    r1.update(x=1, height=10, y=2, width=50)
    print(r1)
