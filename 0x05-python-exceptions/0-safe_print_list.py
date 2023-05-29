#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    result = 0
    try:
        for n in range(x):
            print(f"{my_list[n]}", end='')
            result += 1
    except IndexError:
        pass
    print('')
    return result
