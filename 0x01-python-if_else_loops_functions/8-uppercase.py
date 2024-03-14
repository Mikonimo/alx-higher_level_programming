#!/usr/bin/python3
def uppercase(str):
    """
    Prints a string in uppercase.
    Args:
        str: The string to convert to uppercase.
    """
    uppercase_str = ""
    for char in str:
        if 'a' <= char <= 'z':  # Check if char is lowercase
            uppercase_str += chr(ord(char) - 32)  # Convert to uppercase
        else:
            uppercase_str += char
    print("{}".format(uppercase_str))
