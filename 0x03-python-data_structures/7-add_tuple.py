#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a is None or tuple_b is None:
        return None
    if len(tuple_a) < 2:
        tuple_a = modify_tuple(tuple_a)
    elif len(tuple_b) < 2:
        tuple_b = modify_tuple(tuple_b)
    c = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return c


def modify_tuple(tup):
    if len(tup) == 0:
        a = list(tup)
        a.extend([0, 0])
        tup = tuple(a)
        return tup
    elif len(tup) == 1:
        a = list(tup)
        a.append(0)
        tup = tuple(a)
        return tup
