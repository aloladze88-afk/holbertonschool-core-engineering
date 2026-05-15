#!/usr/bin/env python3
"""Defines VerboseList, a list that prints messages when modified."""


class VerboseList(list):
    """A custom list that reports when items are added or removed."""

    def append(self, item):
        """Add one item and print a message."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, items):
        """Add several items and print how many were added."""
        items = list(items)
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        """Remove one item and print a message."""
        if item in self:
            print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Remove and return one item, then print a message."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)