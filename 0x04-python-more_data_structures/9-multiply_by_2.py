#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    A function that returns a new dictionary
    with all values multiplied by 2
    """
    unidic = {}
    for key, value in a_dictionary.items():
        unidic.update({key: (value * 2)})
    return unidic
