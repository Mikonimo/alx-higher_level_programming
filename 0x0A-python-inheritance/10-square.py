#!/usr/bin/python3
"""Inherits from class Rectangle"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Class Square"""
    def __init__(self, size):
        """initializes class square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculates the area of the square"""
        return self.__size * self.__size
