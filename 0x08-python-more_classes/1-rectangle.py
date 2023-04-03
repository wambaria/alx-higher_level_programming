#!/usr/bin/python3
"""class Rectangle deinition"""


class Rectangle:
    """Class Rectangle is declared"""
    def __init__(self, width=0, height=0):
        """Constructor for the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ggetter for private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sstter for private instance attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter for private instance height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for private instance height"""
        if not isinstance(value, int):
            raise TypeError("height must be an  integer")
        elif value < 0:
            raise ValueError("width msut be >= 0")
        else:
            self.__height = value
