#!/usr/bin/python3


def uniq_add(my_list=[]):
   
    new_l = []
    total = 0
    for i in my_list:
        if i not in new_l:
            total += i
            new_l.append(i)
    return total
