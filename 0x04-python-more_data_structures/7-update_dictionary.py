#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds key/value in a dictionary
    Args:
    a_dictionary: the dictionary being evaluated
    key: the key  added or replaced which always be a string
    value: the value added or replaced can be any type
    Return:
    the updated dictionary
    """
    a_dictionary[key] = value
    return (a_dictionary)
