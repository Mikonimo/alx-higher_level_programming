#!/usr/bin/python3
def best_score(a_dictionary):
    """
    Returns a key with the biggest integer value
    Args:-
    a_dictionary: the dictionary being evaluated
    Return: the key with the biggest integer
    """
    best = float('-inf')
    best_st = None
    if a_dictionary is None:
        return (None)
    for k, v in a_dictionary.items():
        if v > best:
            best_st = k
            best = v
    return (best_st)
