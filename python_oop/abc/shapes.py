#!/usr/bin/env python3
"""Defines shapes using abstract classes and duck typing."""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Blueprint for all shapes."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Represents a circle."""

    def __init__(self, radius):
        """Store the circle radius."""
        self.radius = radius

    def area(self):
        """Return the circle area."""
        return pi * self.radius ** 2

    def perimeter(self):
        """Return the circle perimeter."""
        return 2 * pi * self.radius


class Rectangle(Shape):
    """Represents a rectangle."""

    def __init__(self, width, height):
        """Store the rectangle width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return the rectangle area."""
        return self.width * self.height

    def perimeter(self):
        """Return the rectangle perimeter."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of any shape-like object."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
