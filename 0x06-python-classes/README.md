# 0x06-python-classes

This repository contains the source code and instructions for creating Python classes. It contains the following files:

* **[0-square.py](0-square.py)**: Python file that contains a class **Square** that defines a square by its size.
* **[1-square.py](1-square.py)**: Python file that contains a class **Square** that defines a square by its size as well as its area.
* **[2-square.py](2-square.py)**: Python file that contains a class **Square** that defines a square by its size, its area, and a method to print the square.
* **[3-square.py](3-square.py)**: Python file that contains a class **Square** that defines a square by its size, its area, a method to print the square, and a method to change the square's size.
* **[4-square.py](4-square.py)**: Python file that contains a class **Square** that defines a square by its size, its area, a method to print the square, a method to change the square's size, and a method to calculate the square's position.
* **[5-square.py](5-square.py)**: Python file that contains a class **Square** that defines a square by its size, its area, a method to print the square, a method to change the square's size, a method to calculate the square's position, and its area.
* **[README.md](README.md)**: This file.

## Functions

The following table contains a description of each function of the **Square** class:

| Function | Parameters | Return Value | Description
| -------- | ---------- | ------------ | -----------
| __init__ | `self`, `size` | N/A | Initialize a new Square object
| size | `self` | `private` | Return the size of the Square object
| area | `self` | `public` | Return the area of the Square object
| __str__ | `self` | `str` | Return a string representation of the Square object
| __repr__ | `self` | `str` | Return a string representation of the Square object
| __del__ | `self` | N/A | Delete the Square object
| bigger_or_equal | `rect_1`, `rect_2` | `bool` | Return `True` if `rect_1` is greater than or equal to `rect_2`
| position | `self`, `x`, `y` | N/A | Set the position of the Square object
 
Welcome to 0x06-Python-Classes! This README file will provide you an overview of the project, and a detailed look at each step, feature and functions of the project. 

In this project, we will be learning how to write classes in Python. Classes are an important part of object-oriented programming, and they provide a way to structure source code and to logically group data and functions. They help us to reduce code duplication, increase code extensibility, and greatly improve readability. 

#### What You'll Learn

* What is a class in Python
* How to create a class
* How to use `__init__`
* What is an instance attribute
* What is a class attribute
* What is a class method
* What is an instance method
* How to set up inheritance

## Table of Contents

1. [Overview](#overview)
2. [Defining a Class](#defining-a-class)
3. [Using __init__](#using-__init__)
4. [Instance Attributes](#instance-attributes)
5. [Class Attributes](#class-attributes)
6. [Class Methods](#class-methods)
7. [Instance Methods](#instance-methods)
8. [Inheritance and Subclasses](#inheritance-and-subclasses)
9. [References](#references)

## Overview

Object-oriented programming (OOP) is a programming paradigm that uses objects and their interactions to design applications and computer programs. It is an important concept in software engineering, as it helps to create efficient, organized code. To do this, it uses classes, which are collections of code that define the properties and methods of an object. 

Classes are like blueprints for objects. They define the structure and behavior of the objects, and the objects can then be used to create instances of the class. In Python, classes are defined using the keyword `class`. Instances of a class can then be instantiated, which involves creating an object from the class, and assigning it to a variable. 

In this project, we will be looking at how to write classes in Python. We will also be learning about instance and class attributes, class methods and instance methods, and how to set up inheritance. 

## Defining a Class

In Python, classes are defined using the keyword `class`. For example: 

```
class Dog:
  pass
```

This code creates a class called `Dog`. For now, we have not added any properties or methods to this class, so we pass the keyword `pass`. 

Once the class has been defined, an instance of the class can be created. For example: 

```
dog = Dog()
```

The above code creates an instance of the `Dog` class, and assigns it to the variable `dog`.
 
## Using __init__

The `__init__` method is used to initialize an instance of a class. It is called when an instance of the class is created. The syntax of the `__init__` method looks like this: 

```
def __init__(self, args):
    # code goes here
```

The `__init__` method takes two arguments, `self` and `args`. The `self` argument is used to refer to the instance of the class. The `args` argument is used to pass in any additional arguments that are needed to create the instance. 

For example, if we wanted to create a `Dog` class that took a `name` argument, we could use the following code: 

```
class Dog:
    def __init__(self, name):
        self.name = name

dog = Dog('Fido')
```

The above code creates an instance of the `Dog` class, and sets the `name` attribute to `Fido`. 

## Instance Attributes

Instance attributes are attributes that are specific to each instance of a class. They are used to store data about the instance. 

Instance attributes can be defined in the `__init__` method, or added to the instance outside of the `__init__` method. 

For example, we could create an instance attribute called `age` in the `__init__` method like this: 

```
def __init__(self, name, age):
    self.name = name
    self.age = age
```

We can also add attributes outside of the `__init__` method, like this:

```
dog = Dog('Fido')
dog.breed = 'Labrador'
```

The above code creates an instance attribute called `breed`, and sets it to `Labrador`. 

## Class Attributes

Class attributes are attributes that are shared across all instances of a class. They are used to store data that is shared by all instances of the class. 

Class attributes can be defined in the body of the class or outside of the class. 

For example, if we wanted to define a class attribute called `color`, we could use the following code: 

```
class Dog:
    color = 'black'
```

The above code defines a class attribute called `color`, and sets it to `black`. 

## Class Methods

Class methods are methods that are called on the class itself, rather than on an instance of the class. They are used to perform operations that are related to the class itself, rather than to any individual instance of the class. 

Class methods can be defined in the body of the class, and they take the `cls` argument. For example: 

```
class Dog:
    @classmethod
    def list_breeds(cls):
        # code goes here
```

The above code defines a class method called `list_breeds`. 

## Instance Methods

Instance methods are methods that are called on an instance of a class. They are used to perform operations that are related to an individual instance of the class. 

Instance methods can be defined in the body of the class, and they take the `self` argument. For example: 

```
class Dog:
    def bark(self):
        # code goes here
```

The above code defines an instance method called `bark`. 

## Inheritance and Subclasses

Inheritance is a feature of object-oriented programming that allows a class to inherit the attributes and methods of another class. This is done by defining a subclass, which is a class that inherits from another class. 

For example, if we wanted to create a `GoldenRetriever` subclass of the `Dog` class, we could do it like this: 

```
class GoldenRetriever(Dog):
    pass
```

The above code creates a subclass of the `Dog` class called `GoldenRetriever`. 

## Introduction
This project introduces the concept of classes in Python. A class allows you to create your own complex data types that allow you to store related pieces of data and functions. Oftentimes, classes are used to represent real-world objects. With classes, you can create your own custom objects that have their own unique properties and methods.

Classes can be used to create objects that can be passed around in your program. Objects of the same type can be treated in the same way, allowing code to be more organized and easily readable. In this project, you will learn how to create classes in Python and how to use them to create objects.

## Requirements
Before getting started, you will need to have Python installed on your system. Python can be downloaded from the official website. You will also need a code editor such as Visual Studio Code.

## Initializing and Using Classes
In Python, classes are created by using the `class` keyword followed by the name of the class. Inside the class, the `__init__()` method is used to initialize the object.

The `__init__()` method is used to set up the object and is automatically called when an object is created. It takes in parameters such as the object's properties and other objects that the object itself might need.

Once an object has been initialized, it can be used by calling its methods and properties. You can access an object's properties and methods by using the dot operator.

## Instance Variables
Instance variables are variables that are unique to each instance of a class. They can be accessed and modified from within the class and from outside the class. Instance variables are created by defining them inside the `__init__()` method.

## Class Variables
Class variables are variables that are shared among all instances of a class. These variables are declared outside the `__init__()` method. They can be accessed and modified from within the class and from outside the class.

## Class Methods
Class methods are methods that can be called on the class itself. They are defined using the `@classmethod` decorator. Class methods are often used to create factory methods which are used to create objects from the class.

## Static Methods
Static methods are methods that are not associated with any particular object. They are defined using the `@staticmethod` decorator. Static methods are usually used for utility functions or for creating functions that do not need to access any instance or class variables.

## Inheritance
Inheritance is a useful and powerful feature of object-oriented programming that allows you to create new classes from existing classes. A new class can inherit all of the properties and methods of the parent class and can even add its own custom methods and properties.

## Special Methods
Special methods are methods that are defined with the prefix `__` and are used to override or extend the functionality of an existing class. Special methods are often used to create custom objects that behave like built-in objects.

## Conclusion
Python classes are a powerful and useful tool for creating custom objects. They allow you to create objects that have their own unique properties and methods and to extend the functionality of existing classes. With classes, you can make your code more organized and easier to read.
