#!/usr/bin/python3
"""Contains a function that appends a string to a text file"""


def append_write(filename="", text=""):
    """Appends a string at the end of
     atext file and returns the number of characters"""
    with open(filename, mode='a', encoding="utf-8") as file:
        file.write(text)
    return len(text)
