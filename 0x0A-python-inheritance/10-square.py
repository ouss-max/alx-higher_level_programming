#!/usr/bin/python3
"""Defines a Square class."""

from typing import Union
from rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size: int):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        super().__init__(size, size)
        self.__size = size