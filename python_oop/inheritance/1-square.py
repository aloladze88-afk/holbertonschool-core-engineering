#!/usr/bin/env python3
"""Defines the Square class."""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """A square — a rectangle with equal sides."""

    def __init__(self, size):
        """Initialise the square with a single size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
