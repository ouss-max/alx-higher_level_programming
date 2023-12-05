#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for num in matrix:
        for cn in num:
            print("{:d}".format(cn), end=" " if cn != num[-1] else "")
        print()
