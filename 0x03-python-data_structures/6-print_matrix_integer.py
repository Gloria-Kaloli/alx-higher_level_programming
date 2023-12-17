#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for n in range(len(matrix)):
        for z in range(len(matrix[n])):
            print("{:d}".format(matrix[n][z]), end="")
            if z != (len(matrix[n]) - 1):
                print(" ", end="")

        print("")
