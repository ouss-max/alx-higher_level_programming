#!/usr/bin/python3
""" inherit attributes from List"""


class MyList(list):
    """subclass of list"""
    def __init__(self):
        """object intialisation"""
        super().__init__()

    def print_sorted(self):
        """prints the list after being sorted"""
        print(sorted(self))
