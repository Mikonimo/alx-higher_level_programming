#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    Prints all integers of a list, in reverse order
    Args:
    my_list: the list storing the integers
    """
    my_list.reverse()
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
