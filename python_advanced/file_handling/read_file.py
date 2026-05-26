#!/usr/bin/env python3
"""Defines a function that reads a text file."""


def read_file(filename=""):
    """Read a UTF-8 text file and print its contents to stdout."""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
