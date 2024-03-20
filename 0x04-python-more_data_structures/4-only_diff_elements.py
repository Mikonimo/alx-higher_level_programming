#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    Returns a set of common elements present in only one set
    Args:
    set_1: the first set
    set_2: the second set
    Return:
    set of all elements present in only one set
    """
    one_set = set_1 ^ set_2
    return (one_set)
