#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers.
    Args:
    matrix: the matrix of integers
    """
    for r in matrix:
        for c in r:
            print("{:d}".format(c), end='')
            if c != r[-1]:
                print(' ', end='')

        print()
