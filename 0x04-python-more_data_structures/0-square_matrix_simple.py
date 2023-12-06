#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new_matrix = []
    for cl in matrix:
        result = list(map(lambda x: x**2, cl))
        new_matrix.append(result)
    return new_matrix
