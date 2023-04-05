#!usr/bin/python3
class LockedClass:
    __slots__ = ['first_name']

    def __setattr__(self, name, value):
        if not hasattr(self, name) and name != 'first_name':
            raise AttributeError(f"{self.__class__.__name__} does not allow creating new instance attributes")
        super().__setattr__(name, value)
