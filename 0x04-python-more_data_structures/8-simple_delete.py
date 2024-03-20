#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    Deletes a key in a dictionary
    Args:
    a_dictionary: the dictionary being evaluated
    key: the key being deleted
    Return:
    the new updated dictionary
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return (a_dictionary)
