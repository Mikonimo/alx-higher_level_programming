#!/usr/bin/python3
"""Contains the 'Rectangle' Class which inherits from the Base Class"""

from models.base import Base


class Rectangle(Base):
    """This is the Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets the value for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of width"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of height"""
        if (type(value) is not int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets the value for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the value of x"""
        if (type(value) is not int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets the value for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the value of y"""
        if (type(value) is not int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates the area of the rectangle"""
        return (self.__height * self.__width)

    def display(self):
        """Displays the rectangle using # """
        for y in range(self.y):
            print("")
        for h in range(self.__height):
            for x in range(self.x):
                print(" ", end="")
            for w in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """String representation of the class"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"

    def update(self, *args):
        """Assigns an argument to each attribute"""
        self.id = args[0]
        self.width = args[1]
        self.height = args[2]
        self.x = args[3]
        self.y = args[4]
