#!/usr/bin/python3
"""Contains a function that writes to a text file"""


def write_file(filename="", text=""):
    """writes a string to a text file
     and returns the number of characters written"""
    with open(filename, mode='w', encoding="utf-8") as file:
        file.write(text)
    return len(text)
