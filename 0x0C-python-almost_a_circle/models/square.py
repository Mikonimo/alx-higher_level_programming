#!/usr/bin/python3
"""Contains the 'Square class' which  inherits from the Rectangle class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """This is the Square Class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the Square Class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of the Square Class"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Gets the value of size"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the value of size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
