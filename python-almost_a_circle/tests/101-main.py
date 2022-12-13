#!/usr/bin/python3
""" Main function test """
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    list_rectangles = [Rectangle(62, 12), Rectangle(31, 57, 100, 10), Rectangle(62, 10, 100, 17)]
    list_squares = [Square(65), Square(15, 10, 5), Square(12, 6, 19)]

    Base.draw(list_rectangles, list_squares)
