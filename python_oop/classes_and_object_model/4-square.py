#!/usr/bin/env python3
"""Defines a Square class with a size property getter and setter."""


class Square:
    """Represents a square with controlled access to size."""

    def __init__(self, size=0):
        """Initialise via the setter so validation runs at creation."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Validate and set the size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
