#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
   
    k = list(a_dictionary.k())
    k.sort()
    for key in k:
        print("{}: {}".format(key, a_dictionary[key]))
