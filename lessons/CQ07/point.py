"""CQ07 - Intro to Object Oriented Programming."""
from __future__ import annotations
__author__ = "730679279"


class Point:
    """Create a class called 'Point'."""
    x: float
    y: float

    def __init__(self, inp_x: float, inp_y: float):
        """My constructor."""
        self.x = inp_x
        self.y = inp_y
        
    def scale_by(self, factor: int) -> None:
        """Mutate the value of attribute x and y."""
        self.x = self.x * factor
        self.y = self.y * factor

    def scale(self, factor: int) -> Point:
        """Create a new object with the mutated value of attribute x and y of the previous object."""
        return Point(self.x * factor, self.y * factor)