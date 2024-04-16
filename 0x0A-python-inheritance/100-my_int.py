#!/usr/bin/python3
"""Module that int behaves differently"""


class MyInt(int):
    """Class MyInt"""
    def __eq__(self, other):
        """
        Overrides the equality operator.
        Inverts the behavior of the equality operator.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the inequality operator.
        Inverts the behavior of the inequality operator.
        """
        return super().__eq__(other)
