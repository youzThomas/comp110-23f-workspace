"""CQ07 - Intro to Object Oriented Programming."""
from __future__ import annotations
__author__ = "730679279"


class Point:
    """Create a class called 'Point'."""
    x: float
    y: float

    def __init__(self, inp_x: float = 0.0, inp_y: float = 0.0):
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
    
    def __str__(self) -> str:
        """Print out the 'x' value and 'y' value of an object."""
        x_value: str = str(self.x)
        y_value: str = str(self.y)
        result: str = "x: " + x_value + "; " + "y: " + y_value
        return result
    
    def __mul__(self, factor: int | float) -> Point:
        """Operation overloading of '*'."""
        x = self.x * factor
        y = self.y * factor
        pt3 = Point(x, y)
        return pt3
    
    def __add__(self, factor: int | float) -> Point:
        """Operation overloading of '+'."""
        x = self.x + factor
        y = self.y + factor
        new_pt = Point(x, y)
        return new_pt