"""EX07_Dictionary Unit Tests."""


import pytest
from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance

__author__: int = 730679279


def test_invert_one() -> None:
    """Test_invert_one: use case."""
    test_dict_one: dict[str, str] = {"a": "b", "c": "d", "e": "f"}
    assert invert(test_dict_one) == {"b": "a", "d": "c", "f": "e"}


def test_invert_two() -> None:
    """Test_invert_two: use case."""
    test_dict_two: dict[str, str] = {"k": "j", "u": "v"}
    assert invert(test_dict_two) == {"j": "k", "v": "u"}


def test_invert_three() -> None:
    """Test_invert_three: edge case."""
    with pytest.raises(KeyError):
        test_dict_three: dict[str, str] = {"a": "b", "c": "b"}
        invert(test_dict_three)


def test_favorite_color_one() -> None:
    """Test_favorite_color_one: use case."""
    test_dict_color_one: dict[str, str] = {"T": "blue", "J": "green", "k": "blue"}
    assert favorite_color(test_dict_color_one) == "blue"


def test_favorite_color_two() -> None:
    """Test_favorite_color_two: use case."""
    test_dict_color_two: dict[str, str] = {"F": "black", "S": "yellow", "A": "black"}
    assert favorite_color(test_dict_color_two) == "black"


def test_favorite_color_three() -> None:
    """Test_favorite_color_three: edge case."""
    test_dict_color_three: dict[str, str] = {"B": "red", "I": "pink", "U": "red", "G": "pink"}
    assert favorite_color(test_dict_color_three) == "red"


def test_count_one() -> None:
    """Test_count_one: use case."""
    test_list_count_one: list[str] = ["a", "a", "b"]
    assert count(test_list_count_one) == {"a": 2, "b": 1}


def test_count_two() -> None:
    """Test_count_two: use case."""
    test_list_count_two: list[str] = ["a", "b", "c", "d"]
    assert count(test_list_count_two) == {"a": 1, "b": 1, "c": 1, "d": 1}


def test_count_three() -> None:
    """Test_count_three: edge case."""
    test_list_count_three: list[str] = []
    assert count(test_list_count_three) == {}


def test_alphabetizer_one() -> None:
    """Test_alphabetizer_one: use case."""
    test_list_alphabetizer_one: list[str] = ["apple", "good", "chapel"]
    assert alphabetizer(test_list_alphabetizer_one) == {"a": ["apple"], "g": ["good"], "c": ["chapel"]}


def test_alphabetizer_two() -> None:
    """Test_alphabetizer_two: use case."""
    test_list_alphabetizer_two: list[str] = ["table", "clock", "chair", "boy"]
    assert alphabetizer(test_list_alphabetizer_two) == {"t": ["table"], "c": ["clock", "chair"], "b": ["boy"]}


def test_alphabetizer_three() -> None:
    """Test_alphabetizer_three: edge case."""
    test_list_alphabetizer_three: list[str] = []
    assert alphabetizer(test_list_alphabetizer_three) == {}


def test_update_attendance_one() -> None:
    """Test_update_one: use case."""
    test_dict_update_one: dict[str, list[str]] = {"Monday": ["Thomas", "Jack"], "Tuesday": ["Justin"]}
    test_day_one: str = "Monday"
    test_student_one: str = "Jason"
    assert update_attendance(test_dict_update_one, test_day_one, test_student_one) == {"Monday": ["Thomas", "Jack", "Jason"], "Tuesday": ["Justin"]}


def test_update_attendance_two() -> None:
    """Test_update_two: use case."""
    test_dict_update_two: dict[str, list[str]] = {"Monday": ["Fiona", "Andy"], "Tuesday": ["Jacob", "Matthew"]}
    test_day_two: str = "Friday"
    test_student_two: str = "Kevin"
    assert update_attendance(test_dict_update_two, test_day_two, test_student_two) == {"Monday": ["Fiona", "Andy"], "Tuesday": ["Jacob", "Matthew"], "Friday": ["Kevin"]}


def test_update_attendance_three() -> None:
    """Test_update_three: edge case."""
    test_dict_update_three: dict[str, list[str]] = {}
    test_day_three: str = ""
    test_student_three: str = ""
    assert update_attendance(test_dict_update_three, test_day_three, test_student_three) == {}