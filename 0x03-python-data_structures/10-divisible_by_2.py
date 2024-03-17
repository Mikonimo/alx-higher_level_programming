#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    Finds all multiples of 2 in a list
    Args:
    my_list: the list being evaluated
    Return:
    a new list with True of False depending on whether
    the integer at the same position in the original
    list is a multiple of 2
    """
    d_list = []

    for n in range(len(my_list)):
        if my_list[n] % 2 == 0:
            d_list.append(True)
        else:
            d_list.append(False)

    return (d_list)
