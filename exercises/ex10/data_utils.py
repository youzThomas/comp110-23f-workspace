"""Dictionary related utility functions."""

__author__ = "730679279"

from csv import DictReader


def read_csv_rows(name: str) -> list[dict[str, str]]:
    """Read the CSV file row by row."""
    result: list[dict[str, str]] = []
    file_handle = open(name, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], key: str) -> list[str]:
    """Create a list containing every values in a single column."""
    result: list[str] = []
    for row in table:
        result.append(row[key])
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Turn the input into a dictionary making up of columns."""
    result: dict[str, list[str]] = {}
    title: dict[str, str] = table[0]
    for i in title:
        result[i] = column_values(table, i)
    return result


def head(table: dict[str, list[str]], num_of_row: int) -> dict[str, list[str]]:
    """Create a new table with only the first n rows."""
    result: dict[str, list[str]] = {}
    if num_of_row < len(table):
        for header in table:
            add: list[str] = table[header]
            values: list[str] = []
            i: int = 0
            while i < num_of_row:
                values.append(add[i])
                i = i + 1
            result[header] = values
    else:
        result = table
    return result


def select(table: dict[str, list[str]], copy: list[str]) -> dict[str, list[str]]:
    """Create a new table with selected values in the original columns."""
    result: dict[str, list[str]] = {}
    for i in copy:
        result[i] = table[i]
    return result


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combine two tables into a new one."""
    result: dict[str, list[str]] = {}
    for column in table_1:
        result[column] = table_1[column]
    for column in table_2:
        if column in result:
            result[column] += table_2[column]
        else: 
            result[column] = table_2[column]
    return result


def count(value: list[str]) -> dict[str, int]:
    """Create a dictionary which value associate with the count of the value's appearance in the input list."""
    result: dict[str, int] = {}
    for i in value:
        if i in result:
            result[i] = result[i] + 1
        else:
            result[i] = 1
    return result