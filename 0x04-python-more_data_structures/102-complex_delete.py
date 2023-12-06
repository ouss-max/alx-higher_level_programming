#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    keys = list(a_dictionary.keys())

    for v in keys:
        if value == a_dictionary.get(v):
            del a_dictionary[v]

    return (a_dictionary)
