"""EX04 - 'list' Utility Functions."""
__author__ = "730679279"


def all(integer_list: list[int], integer: int) -> bool:
    """Check if the value within the list is the same as the integer."""
    if len(integer_list) == 0:
        return False
    
    tracker: int = 0

    while tracker < len(integer_list):
        if integer_list[tracker] != integer:
            return False
        else:
            tracker = tracker + 1

    return True


def max(input: list[int]) -> int:
    """Find the largest number in a list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    
    max_value: int = input[0]
    position_index: int = 0

    while position_index < len(input):
        if max_value < input[position_index]:
            max_value = input[position_index]
        position_index = position_index + 1

    return max_value


def is_equal(group_one: list[int], group_two: list[int]) -> bool:
    """Check whether two lists are exactly equal to each others."""
    if len(group_one) != len(group_two):
        return False
    else:
        track_one: int = 0

        while track_one < len(group_one):
            if group_one[track_one] != group_two[track_one]:
                return False
            else:
                track_one = track_one + 1
            
        return True
    
