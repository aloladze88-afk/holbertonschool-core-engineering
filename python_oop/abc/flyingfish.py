#!/usr/bin/env python3
"""Demonstrates multiple inheritance with Fish, Bird, and FlyingFish."""


class Fish:
    """Represents a fish."""

    def swim(self):
        """Print the fish swimming action."""
        print("The fish is swimming")

    def habitat(self):
        """Print the fish habitat."""
        print("The fish lives in water")


class Bird:
    """Represents a bird."""

    def fly(self):
        """Print the bird flying action."""
        print("The bird is flying")

    def habitat(self):
        """Print the bird habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Represents a flying fish that inherits from Fish and Bird."""

    def fly(self):
        """Print the flying fish flying action."""
        print("The flying fish is soaring!")

    def swim(self):
        """Print the flying fish swimming action."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Print the flying fish habitat."""
        print("The flying fish lives both in water and the sky!")