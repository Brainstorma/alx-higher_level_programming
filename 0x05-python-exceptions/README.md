# 0x05. Python - Exceptions

Welcome to 0x05. Python - Exceptions! In this project, you will learn the basics of Python Exceptions and how to use them in your own projects.

## What are Exceptions?

Exceptions are errors that occur when a program encounters a problem during its execution. They can be raised explicitly by the programmer or automatically by the interpreter when some type of error is encountered. Exceptions are handled using the “try-except” statement, allowing the programmer to “catch” the exception and take appropriate action.

## Why Should I Use Exceptions?

Using exceptions can help you produce more robust and reliable code. By handling exceptions correctly, you can ensure that your program will not crash unexpectedly when an unexpected error is encountered. In addition, handling exceptions can also make it easier for you to debug your code, since the interpreter will print out information about the type of exception that was raised.

## Types of Exceptions

In Python, there are several built-in exceptions that you can use in your programs. These include: 

- ValueError
- TypeError
- NameError
- ZeroDivisionError
- SyntaxError
- IndentationError
- AttributeError

## Working with Exceptions

When dealing with exceptions, you will usually use the “try-except” statement. This statement allows you to capture the exception and take appropriate action.
Let's take a look at an example:

```
try:
    result = some_function()
except ValueError:
    print('A ValueError occurred!')
```

In this case, if an exception is raised in the “some_function” call, it will be handled by the “except” part of the statement. In this example, we'll simply print out a message letting the user know that an error occurred. You can also handle multiple types of exceptions in the same “try-except” statement:

```
try:
    result = some_function()
except ValueError:
    print('A ValueError occurred!')
except TypeError:
    print('A TypeError occurred!')
```

## Raising Exceptions

In addition to catching exceptions, you can also explicitly “raise” exceptions when certain conditions are met. This makes it easier for you to handle errors in a more organized manner, as you can raise your own exceptions with custom error messages.

For example, if you wanted to check that a certain function argument is a valid number, you could use the following code:

```
def my_function(arg):
    if not isinstance(arg, int):
        raise ValueError('Argument must be an integer!')
```

In this case, if the argument is not an integer, a ValueError will be raised with a custom error message. This allows you to easily handle potential errors in a much more organized manner.
Scripts
1-safe_print_list.py
This script demonstrates how to use a try-except block to catch and handle an exception that occurs when trying to print an element of a list that does not exist.

2-safe_print_integer.py
This script demonstrates how to use a try-except block to catch and handle an exception that occurs when trying to print a variable that is not of type int.

3-safe_print_list_integers.py
This script demonstrates how to use a try-except block to catch and handle an exception that occurs when trying to print the elements of a list of integers.

4-list_division.py
This script demonstrates how to use a try-except block to catch and handle an exception that occurs when trying to divide elements of a list.

5-raise_exception.py
This script demonstrates how to use the raise statement to raise a specific exception, and how to catch and handle that exception using a try-except block.

6-raise_exception_msg.py
This script demonstrates how to use the raise statement to raise a specific exception with a custom error message, and how to catch and handle that exception using a try-except block.

7-safe_print_module.py
This script demonstrates how to use a try-except-finally block to catch and handle an exception that occurs when trying to import a module, and how to use the finally block to ensure that the module is properly closed.

Prototypes for functions written in this project:

| File                             | Prototype                                               |
| -------------------------------- | ------------------------------------------------------- |
| `0-safe_print_list.py`           | `def safe_print_list(my_list=[], x=0):`                 |
| `1-safe_print_integer.py`        | `def safe_print_integer(value):`                        |
| `2-safe_print_list_integers.py`  | `def safe_print_list_integers(my_list=[], x=0):`        |
| `3-safe_print_division.py`       | `def safe_print_division(a, b):`                        |
| `4-list_division.py`             | `def list_division(my_list_1, my_list_2, list_length):` |
| `5-raise_exception.py`           | `def raise_exception():`                                |
| `6-raise_exception_msg.py`       | `def raise_exception_msg(message=""):`                  |
| `100-safe_print_integer_err.py`  | `def safe_print_integer_err(value):`                    |
| `101-safe_function.py`           | `def safe_function(fct, *args):`                        |
| `102-magic_calculation.py`       | `def magic_calculation(a, b);`                          |
| `103-python.c`                   | <ul><li>`void print_python_list(PyObject *p);`</li><li>`void print_python_bytes(PyObject *p);`</li><li>`void print_python_float(PyObject *p);`</li></ul> |

## Conclusion

In this project, you have learned the basics of Python Exceptions and how to use them in your programs. Exceptions can help you produce more reliable and robust code, as well as make it easier for you to debug and handle errors. Additionally, you can also raise your own exceptions with custom error messages.
