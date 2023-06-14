#!/usr/bin/python3
def search_replace(my_list, search, replace):
    ls_copy = [t if t != search else replace for t in my_list]
    return ls_copy
