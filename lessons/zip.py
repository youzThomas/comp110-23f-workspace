"""Combining two lists into a dictionary."""
__author__: int = 730679279


def zip(string_list: list[str], integral_list: list[int]) -> dict[str, int]:
    """Transfer the values in two lists into one dictionary."""
    a: dict = [str, int]

    if (len(string_list) == len(integral_list)):
        tracker: int = 0

        while (tracker < len(string_list)):
            a.update({string_list[tracker]: integral_list[tracker]})
            tracker = tracker + 1
    
    return a