# 0x0A. Python - Inheritance

Inheritance is a key feature of object-oriented programming (OOP) which allows a class to use properties and methods from another class. Inheritance is a powerful tool for code reuse and programming efficiency, allowing developers to create components quickly and accurately.

In this guide, we will introduce the concept of inheritance in Python, discussing the syntax and types of inheritance, and providing some practical examples. 

### Table of Content

- [What is Inheritance?](#what-is-inheritance)
- [Syntax of Inheritance](#syntax-of-inheritance)
- [Types of Inheritance](#types-of-inheritance)
- [Inheritance Examples](#inheritance-examples)

### What is Inheritance?

Inheritance is a mechanism for reusing code, making it easier to maintain and extend existing classes. It works by allowing a programmer to create a class (the child class) that is derived from another class (the parent class). This process is also known as subclassing or deriving a class.

The child class can inherit the properties and methods of the parent class, making the code easier to read, maintain and extend. Inheritance can also help to prevent errors caused by duplicated code in different classes.

### Syntax of Inheritance

Inheritance is declared using the `class` keyword followed by the name of the child class. The parent class of the child class is then placed in parentheses after the child class name.

```python
class ChildClass(ParentClass):
    # Child class statement block
    # ...
```

In this example, the `ChildClass` class is inheriting from the `ParentClass` class. 

### Types of Inheritance

There are several types of inheritance available in Python, each of which has unique features and advantages. 

##### Single Inheritance
Single inheritance is the most common type of inheritance and occurs when a class inherits from a single parent class.

##### Multiple Inheritance
Multiple inheritance occurs when a class inherits from more than one parent class. This type of inheritance can be useful when the properties of a class need to be combined from different sources.

##### Multilevel Inheritance
Multilevel inheritance occurs when a class inherits from a parent class and then has one or more classes derived from it.

##### Hierarchical Inheritance
Hierarchical inheritance occurs when a single parent class is inherited by multiple child classes.

##### Hybrid Inheritance
Hybrid inheritance is a combination of two or more types of inheritance.

### Inheritance Examples

In this section, we’ll look at some examples of inheritance in Python.

##### Example 1: Single Inheritance

This example demonstrates single inheritance, with a `Shape` class that is the parent of the `Circle` class. The `Circle` class inherits the `draw()` method from the `Shape` class, allowing us to use a single method to draw both shapes.

```python
# Parent class
class Shape:
    def draw(self):
        print("Drawing a shape")
 
# Child class
class Circle(Shape):
    pass
 
# Create objects
c = Circle()
c.draw()
```

##### Example 2: Multiple Inheritance

This example demonstrates multiple inheritance, with a `Bird` class that inherits from both the `Animal` and `Wing` classes. This allows us to use the properties and methods of both classes in the `Bird` class.

```python
# Parent classes
class Animal:
    def move(self):
        print("Moving...")
 
class Wing:
    def flap(self):
        print("Flapping wings...")
 
# Child class
class Bird(Animal, Wing):
    pass
 
# Create objects
b = Bird()
b.move()
b.flap()
```

##### Example 3: Multilevel Inheritance

This example demonstrates multilevel inheritance, with a `Dog` class that inherits from the `Animal` class and a `Poodle` class that inherits from the `Dog` class.

```python
# Parent class
class Animal:
    def move(self):
       print("Moving...")
 
# Child class
class Dog(Animal):
    def bark(self):
        print("Barking...")
 
# Grandchild class
class Poodle(Dog):
    pass
 
# Create objects
p = Poodle()
p.move()
p.bark()
```

### Conclusion

In conclusion, inheritance is an important concept in object-oriented programming which allows developers to create components quickly and efficiently. It works by allowing a child class to inherit the properties and methods of a parent class. Python supports several different types of inheritance, including single, multiple, multilevel and hierarchical inheritance.

We hope that this guide has provided an introduction to inheritance in Python, and given you some practical examples to help you understand how it works.
