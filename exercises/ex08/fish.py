"""File to define Fish class"""
from __future__ import annotations
class Fish:
    age: int
    
    def __init__(self, age_in: int = 0):
        self.age = age_in
        return None
    
    def one_day(self):
        self.age += 1
        return None