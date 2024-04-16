#!/usr/bin/python3
"""Module contains the BaseGeometry class"""


class BaseGeometry:
    """The class BaseGeometry"""
    def area(self):
        """area function"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value is an integer
        Args:
            name: always a string
            value: must be an integer
        """
        if (not isinstance(value, int)):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
