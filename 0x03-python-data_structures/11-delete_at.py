#!/usr/bin/python3

/usr/bin/bash: line 1: q: command not found

    if idx < 0 or idx > len(my_list) - 1:
        return my_list

    else:
        del my_list[idx]
    return my_list

def delete_at(my_list=[], idx=0):
   
    if idx < 0 or idx >= len(my_list):
        return my_list
        
    for i in range(len(my_list)):
        if i == idx:
            my_list = my_list[:i] + my_list[i+1:]
            break

    return my_list 
