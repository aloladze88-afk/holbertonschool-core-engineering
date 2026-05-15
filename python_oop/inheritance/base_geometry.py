#!/usr/bin/env python3
"""Defines the BaseGeometry class."""


class BaseGeometry:
    """Foundation class that defines the shared interface for all shapes."""

    def area(self):
        """Raise an exception — concrete shapes must implement their own area()."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a strictly positive integer.

        Args:
            name  -- the parameter name, used verbatim in error messages
            value -- the value to validate
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
