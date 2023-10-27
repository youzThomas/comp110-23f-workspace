"""Test my zip function."""

from lessons.zip import zip

__author__: int = 730679279


def test_one() -> None:
    """Test_one: use case."""
    test_list_one: list[str] = ["a"]
    test_list_two: list[int] = [1]
    assert zip(test_list_one, test_list_two) == {"a": 1}


def test_two() -> None:
    """Test_two: use case."""
    test_list_one: list[str] = ["b", "c", "d"]
    test_list_two: list[int] = [2, 3, 4]
    assert zip(test_list_one, test_list_two) == {"b": 2, "c": 3, "d": 4}


def test_three() -> None:
    """Test_three: edge case."""
    test_list_one: list[str] = ["z", "y"]
    test_list_two: list[int] = [7]
    assert zip(test_list_one, test_list_two) == {}

