#!/usr/bin/python3
"""Inherits from class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle"""
    def __init__(self, width, height):
        """
        Initializes Rectangle width and height
        Args:
            width: the width of the rectangle
            height: the height of the rectangle
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Calculates the area of the rectangle
        Return:
            the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """Returns the string representation of the rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
