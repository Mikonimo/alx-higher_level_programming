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
    if sentence == '':
        char = None
        return (length, char)
    else:
        char = sentence[0]
        return (length, char)
