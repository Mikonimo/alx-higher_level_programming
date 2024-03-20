#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list
    Args:
    my_list: the list being evaluated
    Return:
    the result
    """
    us = set()
    res = 0
    for n in my_list:
        if n not in us:
            us.add(n)
            res += n
    return (res)
