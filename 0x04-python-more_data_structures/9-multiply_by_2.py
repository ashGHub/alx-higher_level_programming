#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    return {k: a_dictionary[k] * 2 for k in sorted(a_dictionary)}
