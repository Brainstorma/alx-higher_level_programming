# 0x07. Python - Test-driven development

Test-driven development (TDD) is an iterative development process that uses automated tests to verify software functionality before code is written. By writing the tests first, developers are able to break down the problem into small, manageable pieces and develop solutions that are focused on solving the problem.

This project offers an introduction to the TDD methodology. The goal is to use Python to create a set of unit tests that validate the behavior of a program.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

In order to follow this project, you need to have a working Python environment with the following packages installed:

* pytest 
* mock

### Installing

Clone this repository to your local machine: 

```
git clone https://github.com/brainstorma/REPO.git
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
