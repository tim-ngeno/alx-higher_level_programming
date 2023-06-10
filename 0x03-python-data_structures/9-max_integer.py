#!/usr/bin/python3
def max_integer(my_list=[]):
    num = 0
    if my_list is None:
        return None
    for n in my_list:
        if n > num:
            num = n
    return num
