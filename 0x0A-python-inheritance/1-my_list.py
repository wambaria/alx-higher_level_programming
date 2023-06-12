#!/usr/bin/python3
"""
Contains definition for class MyList that inherits from list.
"""


class MyList(list):
    """def for class MyList that inherits from list"""
    def print_sorted(self):
        """Prints list elements in ascending order"""

        sortedlist = sorted(self)
        print(sortedlist)
