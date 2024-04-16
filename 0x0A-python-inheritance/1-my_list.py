#!/usr/bin/python3
"""A class that inherits"""


class MyList(list):
    """My list class"""
    def print_sorted(self):
        """Prints the list in ascending sort"""
        print(sorted(self))
