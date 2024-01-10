#!/usr/bin/python3
""" a function that check if two object are the same type"""


def is_same_class(obj, a_class):
    """check if an object is exactly an instance of the specified class"""
    if type(obj) != a_class:
        return False
    return True
