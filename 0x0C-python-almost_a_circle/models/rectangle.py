#!/usr/bin/python3
"""Contains the 'Rectangle' Class which inherits from the Base Class"""
from models.base import Base


class Rectangle(Base):
    """This is the Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets the value for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of width"""
        self.__width = value

    @property
    def height(self):
        """Gets the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of height"""
        self.value__height = value

    @property
    def x(self):
        """Gets the value for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the value of x"""
        self.__x = value

    @property
    def y(self):
        """Gets the value for y"""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
