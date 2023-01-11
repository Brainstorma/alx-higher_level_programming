#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    last_char = None
    for char in reversed(roman_string):
        if last_char and roman_numerals[char] < roman_numerals[last_char]:
            result -= roman_numerals[char]
        else:
            result += roman_numerals[char]
        last_char = char
    return result
