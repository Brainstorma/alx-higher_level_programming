# 0x07. Python - Test-driven development

Test-driven development (TDD) is an iterative development process that uses automated tests to verify software functionality before code is written. By writing the tests first, developers are able to break down the problem into small, manageable pieces and develop solutions that are focused on solving the problem.

This project offers an introduction to the TDD methodology. The goal is to use Python to create a set of unit tests that validate the behavior of a program.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

## Tests :

* [tests](./tests): Folder of test files. Includes both ALX-provided ones as well as the following eight independently-developed:
  * [0-add_integer.txt](./tests/0-add_integer.txt)
  * [2-matrix_divided.txt](./tests/2-matrix_divided.txt)
  * [3-say_my_name.txt](./tests/3-say_my_name.txt)
  * [4-print_square.txt](./tests/4-print_square.txt)
  * [5-text_indentation.txt](./tests/text_indentation.txt)
  * [6-max_integer_test.py](./tests/6-max_integer_test.py)
  * [100-matrix_mul.txt](./tests/100-matrix_mul.txt)
  * [101-lazy_matrix_mul.txt](./tests/101-lazy_matrix_mul.txt)

## Function Prototypes :

Prototypes for functions written in this project:

| File                     | Prototype                                    |
| ------------------------ | -------------------------------------------- |
| `0-add_integer.py`       | `def add_integer(a, b=98):`                  |
| `2-matrix_divided.py`    | `def matrix_divided(matrix, div):`           |
| `3-say_my_name.py`       | `def say_my_name(first_name, last_name=""):` |
| `4-print_square.py`      | `def print_square(size):`                    |
| `5-text_indentation.py`  | `def text_indentation(text):`                |
| `100-matrix_mul.py`      | `def matrix_mul(m_a, m_b):`                  |
| `101-lazy_matrix_mul.py` | `def lazy_matrix_mul(m_a, m_b):`             |
| `102-python.c`           | `void print_python_string(PyObject *p);`     |

### Prerequisites

In order to follow this project, you need to have a working Python environment with the following packages installed:

* pytest 
* mock

### Installing

Clone this repository to your local machine: 

```
git clone https://github.com/brainstorma/alx-higher_level_programming/0x07-python-test_driven_development.git
```

Once you have the source code, enter the project directory and run the setup script:

```
python setup.py install
```

This command will install the required packages and dependencies into your Python environment.

## Running the tests

Once the setup is complete, you can run the tests with the following command:

```
pytest
```

This command will run all the tests defined in the project. Each test should produce an output in the form of a dot (.) if everything is working as expected.

## Writing Tests

In order to add new tests, you need to add them to the `tests/` directory. All the tests should be placed in separate files and each test file should include the `@pytest.mark.test` annotation. This annotation is used to indicate that the test should be run when `pytest` is executed.

The main purpose of a test is to validate the behavior of a piece of code. Each test should include verification checks to ensure that the code behaves as expected.

## Requirements

This project requires some familiarity with Python, specifically version 3.7 or higher, and the following modules: 
- `unittest`
- `doctest`
- `pytest`

## Files

Below is a list of the files contained in this project, along with a brief description of each:

- `0-add_integer.py`: This file contains a function called `add_integer` that adds two integer values together and returns the sum. 
- `2-matrix_divided.py`: This file contains a function called `matrix_divided` that divides all elements in a given matrix. 
- `3-say_my_name.py`: This file contains a function called `say_my_name` that prints the first and last name of a given person. 
- `4-print_square.py`: This file contains a function called `print_square` that prints a square made of hashes. 
- `5-text_indentation.py`: This file contains a function called `text_indentation` that prints a given paragraph with two new lines after the end of each of the following punctuation marks: `.`, `?`, `:`. 
- `tests/`: This directory contains the test files for each of the functions listed above.

## Tests

The tests for each of the functions contained in this project are located in the `tests/` directory. Each test file contains a series of tests that check the functionality of each function. The goal is to write code that will pass all of the tests in each file.

## How to Run the Tests

To run the tests contained in this project, use the following command:

```
python3 -m unittest discover tests
```

This command will run all the tests in the `tests/` directory and output the results.

## Contributing

If you would like to contribute to this project, please fork the repository, create a feature branch, make your changes, and submit a pull request.
