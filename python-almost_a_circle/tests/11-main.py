#!/usr/bin/python3
""" main function test """
from models.square import Square

if __name__ == "__main__":

    s1 = Square(10)
    print(s1)

    s1.update(20)
    print(s1)

    s1.update(1, 2)
    print(s1)

    s1.update(1, 2, 3)
    print(s1)

    s1.update(1, 2, 3, 4)
    print(s1)

    s1.update(x=7)
    print(s1)

    s1.update(size=5, y=1)
    print(s1)

    s1.update(size=5, id=50, y=1)
    print(s1)
