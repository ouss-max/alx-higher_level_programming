#!/usr/bin/python3


def best_score(a_dictionary):
   
    if a_dictionary:
        new_l = list(a_dictionary.keys())
        my_score = 0
        top = ""
        for i in new_l:
            if a_dictionary[i] > my_score:
                my_score = a_dictionary[i]
                top = i
        return top
