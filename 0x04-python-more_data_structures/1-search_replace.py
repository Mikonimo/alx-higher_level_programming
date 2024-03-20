#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of an element by another
    in a new list
    Args:
    my_list: the initial list
    search: the element to replace in this list
    replace: the new element
    Return:
    the new list
    """
    new_list = []
    for n in range(len(my_list)):
        if my_list[n] == search:
            new_list.append(replace)
        else:
            new_list.append(my_list[n])
    return (new_list)
