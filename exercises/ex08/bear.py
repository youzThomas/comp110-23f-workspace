"""File to define Bear class."""
from __future__ import annotations


class Bear:
    """The Bear class."""
    age: int
    hunger_score: int
    
    def __init__(self, age_in: int = 0, hunger_in: int = 0):
        """Method to create Bear objects."""
        self.age = age_in
        self.hunger_score = hunger_in
        return None
    
    def one_day(self):
        """Method modifying the attributes of a bear after one day."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Method modifying the hunger level of a bear."""
        self.hunger_score = self.hunger_score + num_fish
        return None
    
