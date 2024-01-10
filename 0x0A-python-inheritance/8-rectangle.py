#!/usr/bin/python3
"""declare a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """initiat the rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize the new Rectangle.

        Args:
            width type (int): The width of the rectangle.
            height tyoe (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
