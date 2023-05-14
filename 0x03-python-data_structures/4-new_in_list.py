#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if not my_list:
        return None
    my_list_cp = my_list.copy()
    if (idx < 0 or idx >= len(my_list_cp)):
        return my_list_cp
    my_list_cp[idx] = element
    return my_list_cp
