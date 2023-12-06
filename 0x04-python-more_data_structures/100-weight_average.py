#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    nm = 0
    m = 0

    for i in my_list:
        nm += i[0] * i[1]
        m += i[1]

    return (nm / m)
