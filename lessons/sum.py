"""In - Class Practice - Sum."""
__author__ = "730679279"


def w_sum(vals: list[float]) -> float:
    """Use while loop to add up all numbers in a list"""
    count: int = 0
    sum: float = 0.0
    while count < len(vals):
        sum = sum + vals[count]
        count = count + 1
    
    return sum


def f_sum(vals: list[float]) -> float:
    """Use for loop to add up all numbers in a list"""
    sum: float = 0.0
    for x in vals:
        sum = sum + x
    
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Use for-range loop to add up all numbers in a list"""
    sum: float = 0.0
    x = range(len(vals))
    for element in x:
        sum = sum + element

    return sum



        
