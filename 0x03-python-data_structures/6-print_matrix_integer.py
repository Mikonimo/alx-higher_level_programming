#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers.
    Args:
    matrix: the matrix of integers
    """
    for r in matrix:
        for c in r:
            if c != 0:
                print(' ', end='')
            print("{:d}".format(c), end='')
        print()
