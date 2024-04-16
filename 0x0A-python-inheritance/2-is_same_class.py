#!/usr/bin/python3
"""checks whether the object instance is of the class"""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly and instance
    of the specified class, otherwise False"""
    return type(obj) is a_class
