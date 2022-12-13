#!/usr/bin/python3
""" main function test """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(9, 10, 3)
    r1_dictionary = r1.to_dictionary()
    r2 = Rectangle.create(**r1_dictionary)
    print(r1)
    print(r2)
    print(r1 is r2)
    print(r1 == r2)
