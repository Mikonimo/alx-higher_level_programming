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
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"

    @property
    def size(self):
        """Gets the value of size"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the value of size"""
        self.width = value
        self.height = value
