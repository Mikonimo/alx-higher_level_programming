#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    Prints a dictionary by ordered keys
    Args:
    a_dictionary: the dictionary being evaluated
    """
    s_dictionary = sorted(a_dictionary)
    for k in s_dictionary:
        print("{}: {}".format(k, a_dictionary[k]))
