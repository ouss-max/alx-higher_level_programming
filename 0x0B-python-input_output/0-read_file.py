#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(file_name=""):
    """Print the contents of a UTF8 text file to stdout."""
    with open(file_name, encoding="utf-8") as file:
        print(file.read(), end="")
