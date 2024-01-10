#!/usr/bin/python3
"""function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """Add new attribute to an object if possible.

    Args:
        obj type (any): The object
        att  type (str): the attr name
        value type (any): the attr value
    Raises:
        TypeError: if adding the attribute has failed
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
