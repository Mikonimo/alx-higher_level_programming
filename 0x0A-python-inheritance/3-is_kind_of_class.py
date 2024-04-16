#!/usr/bin/python3
"""checks whether an object is an instance of a specified class"""


def is_kind_of_class(obj, a_class):
    """Return True if the object is an instance of or inherited
    from class specified"""
    return isinstance(obj, a_class)