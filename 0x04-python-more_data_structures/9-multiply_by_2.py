#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    Returns a new dictionary with all values multiplied by 2
    Args:;
    a_dictionary: dictionay being evaluated
    Return: new dictionary with all values multiplied by 2
    """
    n_dictionary = {}
    for k, v in a_dictionary.items():
        n_dictionary[k] = v*2
    return (n_dictionary)
