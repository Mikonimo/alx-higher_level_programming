#!/usr/bin/python3
def multiple_returns(sentence):
    """
    Returns a tuple with the length of a string
    and its first character
    Args:
    sentence: the sentence being evaluated
    Returns:
    tuple with the length of a string and its first character
    """
    length = len(sentence)
    char = sentence[0]
    if length == 0:
        char = None
        return (length, char)
    else:
        return (length, char)
