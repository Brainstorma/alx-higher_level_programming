#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    s = 0
    w = 0

    for t in my_list:
        s += t[0] * t[1]
        w += t[1]

    return s/w
