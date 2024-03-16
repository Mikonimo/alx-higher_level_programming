#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    Replaces an element in a list at a specific position
    without modifying the original list
    Args:
    my_list: the list being evaluated
    idx: the index of the element being replaced
    element: the new element
    """
    if idx < 0 or idx >= len(my_list):
        return (my_list[:])
    else:
        my_list.copy()
        my_list[idx] = element
        return (my_list[:])
