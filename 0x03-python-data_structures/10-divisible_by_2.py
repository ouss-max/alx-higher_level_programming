#!/usr/bin/python3

def divisible_by_2(my_list=[]):

    max_l = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            max_l.append(True)
        else:
            max_l.append(False)
    return max_l
