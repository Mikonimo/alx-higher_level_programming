#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    Converts a Roman numeral to an integer
    Args:;
    roman_string: the roman numeral
    Return: an integer, if roman string is not a string
    or is none 0
    """
    if roman_string is None or not isinstance(roman_string, str):
        return (0)
    roman_numerals = {'I': 1, 'V': 5, 'C': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    final_int = 0
    prev_int = 0
    for rN in reversed(roman_string):
        int = roman_numerals.get(rN, 0)
        if int < prev_int:
            final_int -= int
        else:
            final_int += int
        prev_int = int
    return (final_int)
