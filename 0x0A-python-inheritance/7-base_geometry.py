#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """declare base geometry."""

    def area(self):
        """Non implemented yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """

        Args:
            name type (str): The name of the parameter.
            value type (int): The parameter to validate.
        Raises:
            TypeError: If value isn't an integer.
            ValueError: If value less or equal 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
