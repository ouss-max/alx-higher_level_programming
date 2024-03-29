#!/usr/bin/python3
"""class Student."""


class Student:
    """Representation"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ a dictionary representation"""
        return self.__dict__
