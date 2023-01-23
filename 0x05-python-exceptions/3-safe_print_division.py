#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        value = a / b
    except ZeroDivisionError:
        value = None
    finally:
        if value is not None:
            print("Inside result: {}".format(value))
        return value
