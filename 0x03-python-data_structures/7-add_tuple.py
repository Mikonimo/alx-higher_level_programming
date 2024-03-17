#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    Adds two tuples
    Args:
    tuple_a: the first operand
    tuple_b: the secon(d operand
    Returns:
    a tuple with two integers
    """
    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            tuple_a = 0, 0
        else:
            tuple_a = tuple_a[0], 0
    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            tuple_b = 0, 0
        else:
            tuple_b = tuple_b[0], 0

    tuple_n = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    return (tuple_n)
