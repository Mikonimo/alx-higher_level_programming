#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    Finds the biggest integer of a list
    Args:
    my_list: the list being evaluated
    Return:
    the biggest integer else None
    """
    if len(my_list) == 0:
        return None
    else:
        bigint = my_list[0]
        for n in range(len(my_list[:])):
            if my_list[n] > bigint:
                bigint = my_list[n]
        return (bigint)
