#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """Return True if the object is an instance of or inherited
    from class specified"""
    if (isinstance(obj, a_class) or issubclass(obj, a_class)):
        return True
    else:
        return False
