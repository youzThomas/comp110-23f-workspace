"""EX06_Dictionary."""
__author__: int = 730679279


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Invert the keys and values in the input dictionary."""
    output_dict: dict[str, str] = {}
    for key in input_dict:
        if input_dict[key] not in output_dict:
            output_dict[input_dict[key]] = key
        else:
            raise KeyError("Same key exist mutiple times!")
    return output_dict


def favorite_color(dict1: dict[str, str]) -> str:
    """Find out the color appears the most."""
    track: dict[str, int] = {}
    for item in dict1:
        if dict1[item] not in track:
            track[dict1[item]] = 1
        else:
            track[dict1[item]] = track[dict1[item]] + 1
    max_color: str = ""
    max_count: int = 0
    for item in track:
        if track[item] > max_count:
            max_color = item
            max_count = track[item]
    return str(max_color)


def count(input_list: list[str]) -> dict[str, int]:
    """Count numbers of appearance of each element in the list."""
    result: dict[str, int] = {}
    for i in input_list:
        if i in result:
            result[i] = result[i] + 1
        else:
            result[i] = 1
    return result


def alphabetizer(input_list: list[str]) -> dict[str, list[str]]:
    """Classify each word in the list regarding their first letter."""
    alphabet_dict: dict[str, list[str]] = {}
    for i in input_list:
        if i[0].lower() in alphabet_dict:
            alphabet_dict[(i[0].lower())].append(i)
        else:
            alphabet_dict[i[0].lower()] = [i]
    return alphabet_dict    


def update_attendance(attendance_record: dict[str, list[str]], weekdays: str, student: str) -> dict[str, list[str]]:
    """Update the attendance log by inserting the name of the student into the provided weekday."""
    if weekdays in attendance_record:
        if student not in attendance_record[(weekdays)]:
            attendance_record[(weekdays)].append(student)
    else:
        attendance_record[weekdays] = [student]
    return attendance_record