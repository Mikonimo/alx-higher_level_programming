#!/usr/bin/python3
def no_c(my_string):
    """
    Removes all characters c and C from a string
    Args:
    my_string: the string being evaluated
    Returns:
    the new string
    """
    new_string = ''
    for ch in my_string[:]:   
        if ch != 'c' and ch != 'C':
            new_string += ch
    return (new_string)
