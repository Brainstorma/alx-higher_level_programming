# 0x0C-python-almost_a_circle

## What Is 0x0C-python-almost_a_circle

0x0C-python-almost_a_circle is a Python module that defines a series of classes for representing geometric shapes as Python objects. Its classes may also be used as a base for creating new Python objects representing other geometric shapes.

## Overview of 0x0C-python-almost_a_circle

### Class Hierarchy

The 0x0C-python-almost_a_circle module consists of the following classes, represented as a hierarchy:

**Base**
* Rectangle
* Square

The **Base** class is the base class for all the other classes. All the other classes inherit from **Base**, meaning that they have all the same attributes and methods.

### Attributes

The 0x0C-python-almost_a_circle module defines the following attributes associated with shapes:

* id
* width
* height
* x
* y

The `id` attribute is a unique identifier for each instance of a class. The `width`, `height`, `x`, and `y` attributes are specific to each instance of a class and are used for defining the size and position of the shape on a two-dimensional plane.

### Methods

The 0x0C-python-almost_a_circle module defines the following methods along with their associated parameters:

* `__init__(self, id=None, width=0, height=0, x=0, y=0)`
  * __Arguments__: `self`: the instance of the class that the method is being called on 
    * `id`: the unique identifier of the instance
    * `width`: the width of the shape
    * `height`: the height of the shape
    * `x`: the x coordinate of the shape
    * `y`: the y coordinate of the shape
  * __Returns__: None

* `area(self)`
  * __Arguments__: `self`: the instance of the class that the method is being called on
  * __Returns__: the area of the shape

* `display(self)`
  * __Arguments__: `self`: the instance of the class that the method is being called on
  * __Returns__: None
    
* `__str__(self)`
  * __Arguments__: `self`: the instance of the class that the method is being called on
  * __Returns__: a string representation of the shape

* `update(self, id=None, width=0, height=0, x=0, y=0)`
  * __Arguments__: `self`: the instance of the class that the method is being called on 
    * `id`: the unique identifier of the instance
    * `width`: the width of the shape
    * `height`: the height of the shape
    * `x`: the x coordinate of the shape
    * `y`: the y coordinate of the shape
  * __Returns__: None

* `to_dictionary(self)`
  * __Arguments__: `self`: the instance of the class that the method is being called on
  * __Returns__: a dictionary containing the attributes of the shape

### Instantiating Objects

The 0x0C-python-almost_a_circle module provides the ability to instantiate objects representing geometric shapes by using the class names as functions. The following code will instantiate an object representing a square with a `width` of 5 and an `id` of 42:

```
my_square = Square(width=5, id=42)
```

## Testing 0x0C-python-almost_a_circle

0x0C-python-almost_a_circle includes several test functions for testing the various classes and methods that are part of the module. The tests are written using the `unittest` module, which provides a framework for organizing and running test cases.

### Test Functions

The 0x0C-python-almost_a_circle module includes the following test functions:

* `test_base_attributes` - Tests the `id`, `width`, `height`, `x`, and `y` attributes of the `Base` class

* `test_base_methods` - Tests the `__init__`, `area`, `display`, `__str__`, `update`, and `to_dictionary` methods of the `Base` class

* `test_rectangle_attributes` - Tests the `id`, `width`, `height`, `x`, and `y` attributes of the `Rectangle` class

* `test_rectangle_methods` - Tests the `__init__`, `area`, `display`, `__str__`, `update`, and `to_dictionary` methods of the `Rectangle` class

* `test_square_attributes` - Tests the `id`, `width`, `height`, `x`, and `y` attributes of the `Square` class

* `test_square_methods` - Tests the `__init__`, `area`, `display`, `__str__`, `update`, and `to_dictionary` methods of the `Square` class

### Running Tests

The 0x0C-python-almost_a_circle tests can be run using the following command:

```
python3 -m unittest 0x0C-python-almost_a_circle
```

## What is 0x0C-python-almost_a_circle?

0x0C-python-almost_a_circle is a project that represents an introduction to object-oriented programming for Python. It builds upon basic knowledge of Python and attempts to teach a more advanced level of programming. 0x0C-python-almost__circle uses all the basic concepts of Object Oriented Programming such as classes, objects, and public/private attributes and methods, as well as data encapsulation, inheritance, and polymorphism. This project is ideal for those who have a good understanding of Python and want to take their skills to the next level.

## What does 0x0C-python-almost_a_circle provide?

0x0C-python-almost_a_circle provides the reader with a set of Python classes that help create and use shapes. The shape classes are Rectangle, Square, and Base. Rectangle and Square inherit from class Base, which remains abstract and provides only the data secured through data encapsulation, inheritance, and polymorphism. In addition, 0x0C-python-almost_a_circle also provides two test files in the tests directory, *test_base.py* and *test_models.py*, that allow the user to quickly and easily understand the classes and their instances, as well as their respective functions and methods. 

## What do the test files do?

The files *test_base.py* and *test_models.py* are Python scripts that enable the user to check whether or not the classes and methods being developed are functioning properly. These test scripts are executed to automatically perform a number of tests that verify the correctness and integrity of the code being developed. In the case of *test_base.py*, the tests verify that the Base class hierarchy is correctly defined and that its data values are correctly retrieved and set. Similarly, the *test_models.py* file tests that the Rectangle, Square and Base classes are correctly defined and functioning properly in terms of data retrieval, manipulation and output.

## What resources are available to understand and use 0x0C-python-almost_a_circle?

In order to better understand 0x0C-python-almost_a_circle and use it correctly, it is recommended to have a basic understanding of Python programming and Object-Oriented Programming concepts. Additionally, it is also recommended to refer to the official documentation of Python which can be found here.

For those who are troubled with understanding the classes and methods of 0x0C-python-almost_a_circle, we have compiled a list of resources that will be useful in understanding the project.
* **How to Think Like a Computer Scientist** by Allen B. Downey
* **Head First Python** by Paul Barry 
* **Python Cookbook** by Alex Martelli 
* **Learning Python** by Mark Lutz 
* **Python in a Nutshell** by Alex Martelli 

## Summary

0x0C-python-almost_a_circle is an introductory project in Python Object-Oriented Programming. It provides an understanding of the basics of OOP in Python and also provides two test files (*test_base.py* and *test_models.py*) which enable the user to test their own classes as well as the ones provided in the project. It is recommended for those who want to expand their knowledge in Python and OOP. Resources are available for consultation in understanding and using the project. 

# Enjoy coding with 0x0C-python-almost_a_circle!
