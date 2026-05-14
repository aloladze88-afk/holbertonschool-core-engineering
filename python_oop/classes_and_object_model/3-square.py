#!/usr/bin/env python3

class Square:
    """Represents a square with validated size and area calculation."""

    def __init__(self, size=0):
        """Initialise with optional size, default 0."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):  # ① Public instance method
        """Return the area of the square."""
        return self.__size ** 2  # ② size squared
