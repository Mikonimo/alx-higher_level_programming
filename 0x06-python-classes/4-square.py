#!/usr/bin/python3
"""Define a class square"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Initialize a new square

        Args:
            size (int): The size of the new square.
        """
        self.__size = size

    @property
    def size(self):
        """Retrieve the current size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square
        Args:
            value: the size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Return the current square area
        """
        return (self.__size ** 2)
