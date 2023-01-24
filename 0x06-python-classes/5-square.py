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
        else:
            self.__size = value

    def area(self):
        """Returns the current square area"""
        return (self.__size ** 2)

    def my_print(self):
        """Prints in stdout the square with character #"""

        if self.__size == 0:  # empty line if size is 0
            print()

        for i in range(self.__size):  # prints rows of #s
            for j in range(self.__size):   # prints columns of #s
                print("#", end="")

            print()
