#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds key/value in a dictionary
    Args:
    a_dictionary: the dictionary being evaluated
    key: the key which always be a string
    value: the value can be any type
    Return:
    the updated dictionary
    """
    a_dictionary[key] = value
    return (a_dictionary)
