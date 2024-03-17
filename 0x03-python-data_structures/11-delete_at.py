#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    Deletes an item at a specific position in a list
    Args:
    my_list: the list being evaluated
    idx: the index of the item to be deleted from the list
    Return:
    the new modified list
    if idx is negative or out of range, the same list
    """
    if idx < 0 or idx >= len(my_list):
        return (my_list)

    del my_list[idx]
    return (my_list)
