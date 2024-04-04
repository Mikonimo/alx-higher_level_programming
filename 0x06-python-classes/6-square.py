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

    @property
    def position(self):
        """Retrieve the current positon of the square"""
        return (self.__position)

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

    def my_print(self):
        """Print the square in #"""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
