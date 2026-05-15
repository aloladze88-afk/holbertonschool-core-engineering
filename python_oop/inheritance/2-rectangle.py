#!/usr/bin/env python3
"""Defines the full Rectangle class."""
BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle with area and string representation."""

    def __init__(self, width, height):
        """Initialise and validate width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle description string."""
        return "[Rectangle] {}/{}".format(
            self.__width, self.__height
        )
