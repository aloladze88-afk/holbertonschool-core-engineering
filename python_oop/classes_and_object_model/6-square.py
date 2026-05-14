#!/usr/bin/env python3
"""Defines a Square class."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialise a square with size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the square size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the square size after validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the square position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the square position after validation."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or
                value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Return the square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using #."""
        print(str(self))

    def __str__(self):
        """Return the square as a printable string."""
        if self.__size == 0:
            return ""

        lines = []

        for _ in range(self.__position[1]):
            lines.append("")

        for _ in range(self.__size):
            line = " " * self.__position[0] + "#" * self.__size
            lines.append(line)

        return "\n".join(lines)
