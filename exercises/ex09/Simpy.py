"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730679279"


class Simpy:
    values: list[float]

    def __init__(self, input_value: list[float]) -> None:
        """Constructor."""
        self.values = input_value
    
    def __str__(self) -> str:
        """Overloading print."""
        result: str = "Simple" + " ( " + str(self.values) + " ) "
        return result
    
    def fill(self, fill_value: float, fill_count: int):
        """Fill the 'values' attribute with the given number."""
        i: int = 0
        while i < fill_count:
            self.values.append(fill_value)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0):
        """Fill the 'value' attribute with the given range of numbers."""
        assert step != 0.0
        while abs(start) < abs(stop):
            self.values.append(start)
            start = start + step
        
    def sum(self) -> float:
        """Calculate the sum of elements in 'values' attribute."""
        result: float = sum(self.values)
        return result
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overloading add."""
        if isinstance(rhs, float):
            new_values: list[float] = [i + rhs for i in self.values]
        elif isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            new_values: list[float] = []
            for x in range(len(self.values)):
                new_values.append(self.values[x] + rhs.values[x])
        return Simpy(new_values)
    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overloading power."""
        if isinstance(rhs, float):
            new_values: list[float] = [i ** rhs for i in self.values]
        elif isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            new_values: list[float] = []
            for x in range(len(self.values)):
                new_values.append(self.values[x] ** rhs.values[x])
        return Simpy(new_values)
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Overloading equal."""
        if isinstance(rhs, float):
            result: list[bool] = [x == rhs for x in self.values]
        elif isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            result = [self.values[x] == rhs.values[x] for x in range(len(self.values))]
        return result
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Overloading 'greater than'."""
        if isinstance(rhs, float):
            result: list[bool] = [x > rhs for x in self.values]
        elif isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            result = [self.values[x] > rhs.values[x] for x  in range(len(self.values))]
        return result
    
    def __getitem__(self, rhs: int) -> float:
        """Overloading subscription notation."""
        return self.values[rhs]
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Overloading subscription notation."""
        if isinstance(rhs, int):
            return self.values[rhs]
        elif isinstance(rhs, list) and all(isinstance(item, bool) for item in rhs):
            mask: list[bool] = [self.values[x] for x in range(len(self.values)) if rhs[x]]
        return Simpy(mask)