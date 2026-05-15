#!/usr/bin/env python3
"""Defines an abstract Animal class and two concrete subclasses."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Return the sound made by the animal."""
        pass


class Dog(Animal):
    """Dog class that implements Animal."""

    def sound(self):
        """Return the sound made by a dog."""
        return "Bark"


class Cat(Animal):
    """Cat class that implements Animal."""

    def sound(self):
        """Return the sound made by a cat."""
        return "Meow"
