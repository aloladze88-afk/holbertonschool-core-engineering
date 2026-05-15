#!/usr/bin/env python3
"""Defines mixins and a Dragon class using multiple inheritance."""


class SwimMixin:
    """Provides swimming behaviour."""

    def swim(self):
        """Print a swimming message."""
        print("The creature swims!")


class FlyMixin:
    """Provides flying behaviour."""

    def fly(self):
        """Print a flying message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Represents a dragon that can swim, fly, and roar."""

    def roar(self):
        """Print a roaring message."""
        print("The dragon roars!")