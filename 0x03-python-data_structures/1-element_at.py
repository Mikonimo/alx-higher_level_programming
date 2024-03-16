#!/usr/bin/python3
def element_at(my_list, idx):
    """
    Retrieves an element from a list like in C
    Args:
    my_list: the list being evaluated
    idx: the index of the element in the list
    Returns:
    the element retrieved
    none if idx is negative or it is out of range
    """
    if idx < 0 or idx >= len(my_list):
        return ("None")
    else:
        return my_list([idx])
