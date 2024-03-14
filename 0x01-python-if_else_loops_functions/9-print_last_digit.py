#!/usr/bin/python3
def print_last_digit(number):
    """
    Prints the last digit of a number.
    Args:
        number: The number whose last digit to print.
    Returns:
        The value of the last digit.
    """
    last_digit = abs(number) % 10
    print(last_digit, end="")
    return last_digit
