"""Dictionary related utility functions."""

__author__ = "730679279"

from csv import DictReader

def read_csv_rows(name: str) -> list[dict[str, str]]:
    result: list[dict[str, str]] = []
    file_handle = open(name, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result

def column_values(table: list[dict[str, str]], key: str) -> list[str]:
    result: list[str] = []
    for row in table:
        result.append(row[key])
    return result

def columnar(table: list[dict[str, str]]) -> dict[str,list[str]]:
    result: dict[str, list[str]] = {}
    title: dict[str, str] = table[0]
    for i in title:
        result[i] = column_values(table, i)
    return result

def head(table: dict[str, list[str]], row: int) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    if row < len(table):
        for i in table:
            add: list[str] = table[i]
            value: list[str] = []
            a: int = 0
            while a < row:
                value.append(add[i])
                i = i + 1
                result[i] = value
    else:
        result = table
    return result

def select(table: dict[str, list[str]], copy: list[str]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for i in copy:
        result[i] = table[i]
    return result

def concat(table_one: dict[str, list[str]], table_two: dict[str, list[str]]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for column in table_one:
        result[column] = table_one[column]
    for column in table_two:
        if column in result:
            result[column] = result[column] + table_two[column]
    else:
        result[column] = table_two[column]
    return result

def count(value: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}
    for i in value:
        if i in result:
            result[i] = result[i] + 1
        else:
            result[i] = 1
    return result

