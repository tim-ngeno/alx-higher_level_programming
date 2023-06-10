#!/usr/bin/python3
def max_integer(my_list=[]):
    num = 0
    if my_list is None or len(my_list) == 0:
        return None
    for n in my_list:
        if n > num:
            num = n
    return num
