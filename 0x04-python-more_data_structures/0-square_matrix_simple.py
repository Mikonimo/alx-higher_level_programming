#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix
    Args:
    matrix: the matrix being evaluated
    Return:
    a new matrix
    """
    n_matrix = []
    n_matrix = [[x**2 for x in n] for n in matrix]
    return (n_matrix)
