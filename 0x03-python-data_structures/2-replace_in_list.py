#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    Replaces and element of a list at a specific position
    Args:
    my_list: the list being evaluated
    idx: the index of the element to be replaced
    element: the new element
    Returns:
    the new modified list
    original list if idx is negative or if idx is out of range
    """
    if idx < 0 or idx >= len(my_list):
        return (my_list[:])
    else:
        my_list[idx] = element
        return (my_list[:])
