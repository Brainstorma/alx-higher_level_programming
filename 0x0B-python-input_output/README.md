# 0x0B. Python - Input/Output

### Introduction

This library provides an interface for allowing users to read and write data from various input/output (I/O) sources. It provides tools for performing I/O operations such as opening, closing, reading, and writing to files, as well as many other functions that are commonly used in Python programming. This library is easy to use and provides robust and efficient methods for working with data.

### Features

The library includes the following features:
- Reading and writing data from and to files.
- Specifying the encoding of files when reading and writing.
- Binary data support.
- Controlling the buffering of data when reading or writing.
- Memory mapping of files.
- Low-level access to standard I/O streams.

Prototypes for functions written in this project:

| File        | Prototype               |
| ----------- | ----------------------- |
| `0-read_file.py` | `def read_file(filename=""):` |
| `1-number_of_lines.py` | `def number_of_lines(filename=""):` |
| `2-read_lines.py` | `def read_lines(filename="", nb_lines=0):` |
| `3-write_file.py` | `def write_file(filename="", text=""):` |
| `2-append_write.py` | `def append_write(filename="", text=""):` |
| `3-to_json_string.py` | `def to_json_string(my_obj):` |
| `4-from_json_string.py` | `def from_json_string(my_str):` |
| `5-save_to_json_file.py` | `def save_to_json_file(my_obj, filename):` |
| `6-load_from_json_file.py` | `def load_from_json_file(filename):` |
| `8-class_to_json.py` | `def class_to_json(obj):` |
| `12-pascal_triangle.py` | `def pascal_triangle(n):` |
| `100-append_after.py` | `def append_after(filename="", search_string="", new_string=""):` |

## Tasks :page_with_curl:

* **0. Read file**
  * [0-read_file.py](./0-read_file.py): Python function that prints the contents of a UTF8 text file to standard output.

* **1. Write to a file**
  * [1-write_file.py](./1-write_file.py): Python function that writes a string to a UTF8 text file and returns the number of characters written.

* **2. Append to a file**
  * [2-append_write.py](./2-append_write.py): Python function that appends a string to the end of a UTF8 text file and returns the number of characters appended.

* **3. To JSON string**
  * [3-to_json_string.py](./3-to_json_string.py): Python function that returns the JSON string representation of an object.

* **4. From JSON string to Object**
  * [4-from_json_string.py](./4-from_json_string.py): Python function that returns the Python object represented by a JSON string.

* **5. Save Object to a file**
  * [5-save_to_json_file.py](./5-save_to_json_file.py): Python function that writes an object to a text file using JSON representation.

* **6. Create object from a JSON file**
  * [6-load_from_json_file.py](./6-load_from_json_file.py): Python function that creates an object from a `.json` file.

* **7. Load, add, save**
  * [7-add_item.py](./7-add_item.py): Python script that stores all command line arguments to a Python list saved in the file `add_item.json`.

* **8. Class to JSON**
  * [8-class_to_json.py](./8-class_to_json.py): Python function that returns the dictionary description for simple Python data structures (lists, dictionaries, strings, integers and booleans).

* **9. Student to JSON**
  * [9-student.py](./9-student.py): Python class `Student` that defines a student. Includes:
    * Public instance attributes `first_name`, `last_name`, and `age`.
    * Instantiation with `first_name`, `last_name`, and `age`: `def __init__(self, first_name, last_name, age):`.
    * Public method `def to_json(self):` that returns the dictionary representation of a `Student` instance.

* **10. Student to JSON with filter**
  * [10-student.py](./10-student.py): Python class `Student` that defines a student. Builds on [11-student.py](./11-student.py) with:
    * Public method `def to_json(self, attrs=None):` that returns the dictionary representation of a `Student` instance.
    * If `attrs` is a list of strings, only the attributes listed are represented in the dictionary.

* **11. Student to disk and reload**
  * [11-student.py](./11-student.py): Python class `Student` that defines a student. Builds on [12-student.py](./12-student.py) with:
    * Public method `def reload_from_json(self, json):` that replaces all attributes of the `Student` instance using the key/value pairs listed in `json`.
    * The method assumes `json` is a dictionary containing attributes with name/value corresponding to key/value.

* **12. Pascal's Triangle**
  * [12-pascal_triangle.py](./12-pascal_triangle.py): Python function that returns a list of lists of integers representing Pascal's triangle of size `n`.
  * Assumes the size parameter `n` is an integer.
  * If `n` is less than or equal to `0`, returns an empty list.

* **13. Search and update**
  * [100-append_after.py](./100-append_after.py): Python function that inserts a line of text to a file after each line containing a specified string.

* **14. Log parsing**
  * [101-stats.py](./101-stats.py): Python script that reads lines from standard input. After every 10 lines or the input of a keyboard interruption (`CTRL + C`), computes the following metrics:
    * Total file size up that point: `File size: <total size>`
    * Status code of each read line, printed in ascending order:  `<status code>: <number>`
  * Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
  <status code> <file size>`

### Installation

The library can be installed using the pip package manager:

```
pip install 0x0B-python-input_output
```

### Usage

In order to use the library, users must first import the library:

```python
import io
```

Once the library has been imported, users can access all of the available methods and functions.

### Examples

The following example demonstrates how to open and read from a file:

```python
# Open a file for reading
f = io.open("myfile.txt")

# Read the contents of the file
data = f.read()

# Close the file
f.close()
```

The following example demonstrates how to write to a file:

```python
# Open a file for writing
f = io.open("myfile.txt", "w")

# Write some data to the file
f.write("Hello, World!")

# Close the file
f.close()
```

### API Reference

The API reference documentation can be found [here](https://docs.python.org/2/library/io.html).

### Resources

https://docs.python.org/2/library/io.html

https://pymotw.com/2/io/

In this guide, you will learn about Python Input/Output, which includes topics such as:
- How to get data in and out of Python
- How to read and write to files
- How to format data for output
- How to use Python modules for I/O
- How to use functions, classes and objects for I/O
- How to do error handling


## Getting Started

To get started with Python I/O, you’ll need to make sure you have Python installed on your system. You can install Python from [here](https://www.python.org/).

Once you have Python installed, you can open the Python interpreter by typing `python` in the command line. From here, you can enter or exit Python commands.

After you have the Python interpreter open, let’s look at some basic input/output operations.


## Input/Output Basics

Python has a variety of ways to get data in and out of the language. We’ll look at the most commonly used methods.

### Printing Output

The most basic way to output something is to use the `print` function. The `print` function will take any number of arguments and print them out on the screen.

Let’s try it out:

```
>>> print("Hello World")
Hello World
```

The `print` function can also take multiple arguments. It will separate them with a space, and then print them out on the same line.

```
>>> print("Hello", "World")
Hello World
```

If you want to print out multiple lines, you can use the `end` argument with the `print` function.

```
>>> print("Hello", end="\n")
Hello
>>> print("World")
World
```

### Getting Input

Python also supports getting input from the user. To get input from the user, you can use the `input` function. 

The `input` function will read a line from the user and return that line as a string.

```
name = input("What is your name? ")
print("Hello", name)
What is your name? Michael
Hello Michael
```

### Formatted Output

You can also use the `format` function to format strings for output. The `format` function takes a string and a number of arguments and formats the string with the given arguments.

For example, you can use the `format` function to format a string like this:

```
name = "Michael"
age = 32

formatted_string = "My name is {}, and I am {} years old.".format(name, age)

print(formatted_string)
My name is Michael, and I am 32 years old.
```

The `format` function allows you to easily format strings for output.


## Files

Python also supports reading and writing to files. To do this, you’ll need to use the `open` function.

The `open` function takes two arguments: the name of the file, and the mode. The mode determines whether you’re reading from or writing to the file.

For example, if you wanted to open a file for reading, you would use the `"r"` mode:

```
f = open("my_file.txt", "r")
```

And if you wanted to open a file for writing, you would use the `"w"` mode:

```
f = open("my_file.txt", "w")
```

When you’re done working with the file, you should close it using the `close` function:

```
f.close()
```

Once you have the file open, you can read and write to it using the `read` and `write` functions.

Let’s look at an example of reading a file:

```
f = open("my_file.txt", "r")
contents = f.read()
f.close()

print(contents)
```

This will read the entire contents of the file and then print it out.

Let’s look at an example of writing to a file:

```
f = open("my_file.txt", "w")
f.write("Hello World!")
f.close()
```

This will overwrite the contents of the file with the string “Hello World!”.

You can also use the `append` mode to append data to the end of the file.

```
f = open("my_file.txt", "a")
f.write("Hello Again!")
f.close()
```

This will add the string “Hello Again!” to the end of the file.


## Modules

Python also has a number of modules to make it easier to work with files and other I/O operations.

### os module

The `os` module is a built-in module that provides functions for interacting with the operating system.

For example, you can use the `listdir` function to list the files in a directory:

```
import os

# get a list of files in the current directory
files = os.listdir(".")

# print out each file
for file in files:
    print(file)
```

You can also use the `rename` function to rename a file:

```
import os

# rename a file 
os.rename("old_name.txt", "new_name.txt")
```

### shutil module

The `shutil` module is a built-in module that provides functions for copying and moving files.

You can use the `copy` function to copy a file:

```
import shutil

# copy a file 
shutil.copy("source_file.txt", "destination_file.txt")
```

And you can use the `move` function to move a file:

```
import shutil

# move a file 
shutil.move("source_file.txt", "destination_file.txt")
```

### pickle module

The `pickle` module is a built-in module that provides functions for serializing and deserializing objects. 

You can use the `dump` function to serialize an object:

```
import pickle

# serialize an object
my_data = {'name': 'John', 'age': 32}

pickle.dump(my_data, open("my_data.pickle", "wb"))
```

And you can use the `load` function to deserialize an object:

```
import pickle

# deserialize an object
my_data = pickle.load(open("my_data.pickle", "rb"))

print(my_data)
{'name': 'John', 'age': 32}
```

## Functions, Classes and Objects

Python also supports using functions, classes and objects for I/O operations.

### Functions

You can write your own functions to do I/O operations. For example, you can write a function to read a file:

```
def read_file(filename):
    with open(filename, "r") as f:
        contents = f.read()
    return contents
```

This function takes a filename as an argument, and then reads the contents of the file and returns them as a string.

### Classes

You can also create your own classes to do I/O operations. For example, you can create a class to represent a file:

```
class File:
    def __init__(self, filename):
        self.filename = filename
    
    def read(self):
        with open(self.filename, "r") as f:
            contents = f.read()
        return contents
```

This class has one method, `read`, which will read the contents of the file and return them as a string.

### Objects

Finally, you can also use objects for I/O operations. For example, you can use the `open` function to create a file object:

```
f = open("my_file.txt", "r")
contents = f.read()
f.close()
```

Once you have a file object, you can use it to read and write to a file:

```
f = open("my_file.txt", "r")
contents = f.read()
f.write("Hello World!")
f.close()
```

## Error Handling

When you’re working with I/O operations, it’s important to handle any errors that may occur.

For example, if you’re trying to read a file and the file doesn’t exist, you should handle that error.

You can do this using the `try` and `except` statements:

```
try:
    f = open("my_file.txt")
    contents = f.read()
except FileNotFoundError:
    print("File not found!")
```

This will attempt to open the file, and if it fails, it will print out an error message.

## Conclusion

In this guide, we’ve looked at Python Input/Output, including how to get data in and out of Python, how to read and write to files, how to format data for output, how to use Python modules for I/O, how to use functions, classes and objects for I/O, and how to do error handling.

We hope this guide was helpful, and now you’re ready to go out and start working with Python I/O!

The 0x0B. Python - Input/Output library provides a comprehensive set of tools for performing I/O operations with data. By using this library, users are able to easily read, write, and manipulate data from various sources. It is easy to use and provides robust and efficient methods for working with data.
