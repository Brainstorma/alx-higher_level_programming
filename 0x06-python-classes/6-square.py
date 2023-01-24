 class Square:
    """Defines a square by size and position"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square with optional size and optional position"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:  # valid input for size attribute
            self.__size = value

    @property  # getter for position attribute
    def position(self):  # getter for position attribute
        return self.__position

    @position.setter  # setter for position attribute
    def position(self, value):  # setter for position attribute
        if type(value) is not tuple or len(value) != 2 or type(value[0]) is not int or type(value[1]) is not int or value[0] < 0 or value[1] < 0:   # checks if valid input for position attribute
            raise TypeError("position must be a tuple of 2 positive integers")   # raises exception if invalid input

        else:   # valid input for position attribute

            self.__position = value   # sets the new value to the private instance attribute

    def area(self):   # public instance method that returns current square area

        return self.__size ** 2   # returns current square area (square of side length)

    def my_print(self):   # public instance method that prints in stdout the square with character '#'

        if self.__size == 0:  # checks if side length is zero (empty line)

            print()  # prints empty line

        else:  # side length is greater than zero (non-empty line)

            print('\n' * self.__position[1], end="")  # prints new lines based on y-coordinate of top left corner

            for i in range(self.__size):  # iterates through rows

                print(' ' * self.__position[0], end="")  # prints spaces based on x-coordinate of top left corner

                print('#' * self.__size)
