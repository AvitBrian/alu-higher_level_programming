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

    def update(self, *args, **kwargs):
        """ updates the square """

        if args and len(args) != 0:
            count = 0
            for each in args:
                if count == 0:
                    if each is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = each
                elif count == 1:
                    self.size = each
                elif count == 2:
                    self.x = each
                elif count == 3:
                    self.y = each
                count += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """ dictionary representaion """
        return {
            "id": self.id,
            "size": self.height,
            "x": self.x,
            "y": self.y
        }
