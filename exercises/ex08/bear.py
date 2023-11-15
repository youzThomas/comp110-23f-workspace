"""File to define Bear class"""
from __future__ import annotations
class Bear:
    age: int
    hunger_score: int
    
    def __init__(self, age_in: int = 0, hunger_in: int = 0):
        self.age = age_in
        self.hunger_score = hunger_in
        return None
    
    def one_day(self):
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        self.hunger_score = self.hunger_score + num_fish
        return None
    
