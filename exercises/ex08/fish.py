"""File to define Fish class."""
from __future__ import annotations


class Fish:
    """The Fish class."""
    age: int
    
    def __init__(self, age_in: int = 0):
        """Method to create Fish objects."""
        self.age = age_in
        return None
    
    def one_day(self):
        """Method modifying the age attribute of a fish."""
        self.age += 1
        return None