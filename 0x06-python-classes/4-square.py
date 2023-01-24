#!/usr/bin/python3
 class Square:
    """Defines a square by size"""

    def __init__(self, size=0):
        """Initializes the square with optional size"""
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Returns the current square area"""
        return (self.__size ** 2)
