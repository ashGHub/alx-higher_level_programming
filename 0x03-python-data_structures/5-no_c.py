#!/usr/bin/python3
def no_c(my_string):
    result = ''
    if not my_string:
        return result
    for ch in my_string:
        if (ch != 'c' and ch != 'C'):
            result += ch
    return result
