#!/usr/bin/env python3
"""Defines the Square class with string representation."""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """A square with its own string format."""

    def __init__(self, size):
        """Initialise the square and store size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return the square description string."""
        return "[Square] {}/{}".format(
            self.__size, self.__size
        )
