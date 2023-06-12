#!/usr/bin/python3
"""
contains def of the function lookup
"""

def lookup(obj):

    """Returns list of attributes and methods of an object
    Args:
        obj (any): object whose attributes and methods are to be returned
    """

    return (dir(obj))
