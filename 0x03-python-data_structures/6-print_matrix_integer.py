#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print('\n', end='')
    for row in matrix:
        for c in range(len(row)):
            if c != 0:
                print(" ", end='')
            print("{:d}".format(row[c]), end='')
        print('\n', end='')
