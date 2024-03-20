#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """
    Returns a list with all values multiplied by a
    no without using any loops
    Args:;
    my_list: the list being evaluated
    number: the multipier
    Return: the new updated list after multipication
    """
    new_list = list(map(lambda x: x * number, my_list))
    return (new_list)
