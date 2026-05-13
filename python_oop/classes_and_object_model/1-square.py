#!/usr/bin/env python3
"""Defines a Square class with a private size attribute."""


class Square:
    """Represents a square with a private side length."""

    def __init__(self, size):
        """Initialise the square with a given size."""
        self.__size = size
