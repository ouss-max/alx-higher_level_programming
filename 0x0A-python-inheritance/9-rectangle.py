#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
from typing import Union
from base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width: int, height: int) -> None:
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self) -> int:
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self) -> str:
        """Return the print() and str() representation of a Rectangle."""
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"