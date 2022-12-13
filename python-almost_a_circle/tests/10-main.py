#!/usr/bin/python3
""" main function test """
from models.square import Square

if __name__ == "__main__":

    s1 = Square(10)
    print(s1)
    print(s1.size)
    s1.size = 7
    print(s1)

    try:
        s1.size = "4"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
