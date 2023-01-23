#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
"""Print x elememts of a list.
    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.
    Returns:
        The number of elements printed.
"""
    try:
        printed = 0
        while printed < x:
            print("{}".format(my_list[printed]), end=" ")
            printed += 1
        print()
        return printed
    except IndexError:
        print()
        return printed
