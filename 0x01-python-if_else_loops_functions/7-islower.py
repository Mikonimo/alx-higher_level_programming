#!/usr/bin/python3
def islower(c):
    """
    Checks if a character c is lowercase.
    Args:
        c: The character to check.
    Returns:
        True if c is lowercase, False otherwise.
    """
    return 97 <= ord(c) <= 122
