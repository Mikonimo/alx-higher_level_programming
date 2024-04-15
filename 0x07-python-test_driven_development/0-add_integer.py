#!/usr/bin/python3
"""

This module has a function of adding integer

"""


def add_integer(a, b=98):
    """
    Adds two integers
    Args:
        a: first paramete
        b: second parameter;
    Return: the sum
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
