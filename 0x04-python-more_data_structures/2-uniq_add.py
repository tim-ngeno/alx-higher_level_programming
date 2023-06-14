#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return None
    as_set = set(my_list)
    res = 0
    for x in as_set:
        res += x
    return res
