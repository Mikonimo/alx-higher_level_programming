#!/usr/bin/python3
def is_same_class(obj, a_class):
    """Returns True if the object is exactly and instance
    of the specified class, otherwise False"""
    if (isinstance(obj, a_class)):
        return True
    else:
        return False