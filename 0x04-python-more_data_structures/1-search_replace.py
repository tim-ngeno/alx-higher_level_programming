#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None or len(my_list) == 0:
        return None
    list_copy = my_list[:]
    for idx, elem in enumerate(list_copy):
        if elem == search:
            list_copy[idx] = replace
    return list_copy
