#!/usr/bin/env python3
"""Defines a Square class with size validation."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialise a square with a checked size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
