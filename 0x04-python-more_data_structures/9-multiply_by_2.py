#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for d in a_dictionary:
        new_dictionary[d] = a_dictionary[d] * 2
    return new_dictionary
