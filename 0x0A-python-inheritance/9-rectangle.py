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
        self.__width = width
        self.integer_validator("width", width)
        self.__height = height
        self.integer_validator("height", height)

    def area(self):
        """
        Calculates the area of the rectangle
        Return:
            the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """Returns the string representation of the rectangle"""
        return print("[Rectangle] {self.__width}/{self.__height}")
