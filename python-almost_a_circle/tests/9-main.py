#!/usr/bin/python3
""" main function test """
from models.square import Square

if __name__ == "__main__":

    s1 = Square(10)
    print(s1)
    print(s1.area())
    s1.display()

    print("---")

    s2 = Square(8, 4)
    print(s2)
    print(s2.area())
    s2.display()

    print("---")

    s3 = Square(8, 2, 8)
    print(s3)
    print(s3.area())
    s3.display()
