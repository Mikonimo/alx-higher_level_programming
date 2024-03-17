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
    n_list = []

    if idx < 0 or idx > len(my_list):
        return (my_list)
    else:
        for n in range(len(my_list)):
            if my_list[n] != my_list[idx]:
                n_list.append(my_list[n])
        del my_list[idx]
        return (my_list)
  