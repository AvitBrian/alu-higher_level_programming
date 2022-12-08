#!/usr/bin/python3
""" the square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ represents a square """

    def __init__(self, size, x=0, y=0, id=None):
        """initializaation"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ get/set size """
        return self.height

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
