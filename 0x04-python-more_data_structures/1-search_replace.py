#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None or len(my_list) == 0:
        return None
    ls_copy = my_list[:]
    ls_copy = [t if t != search else replace for t in my_list]
    return ls_copy
