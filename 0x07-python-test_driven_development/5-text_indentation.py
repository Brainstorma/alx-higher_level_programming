#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    jaas = 0
    while jaas < len(text) and text[jaas] == ' ':
        jaas += 1

    while jaas < len(text):
        print(text[jaas], end="")
        if text[jaas] == "\n" or text[jaas] in ".?:":
            if text[jaas] in ".?:":
                print("\n")
            jaas += 1
            while jaas < len(text) and text[jaas] == ' ':
                jaas += 1
            continue
        jaas += 1
