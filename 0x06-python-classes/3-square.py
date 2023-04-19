#!/usr/bin/python3
"""Create a Class Square with size and method of area"""


class Square:
    """Class square is declared"""

    def __init__(self, size=0):
        """Constructor of the square"""
        if (type(size) is not int):
            raise (TypeError("size must be an integer"))
        elif (size < 0):
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = size

    def area(self):
        """Method calculates area of the Square"""
        return (self.__size ** 2)
