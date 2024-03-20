#!/usr/bin/python3
def common_elements(set_1, set_2):
    """
    Returns a set of common elements in two sets
    Args:
    set_1: the first set
    set_2: the second set
    Return:
    set of common elements from set_1 and set_2
    """
    com_set = set_1 & set_2
    return (com_set)
