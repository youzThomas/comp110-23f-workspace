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
    track: dict[str, str] = {}
    for key, value in dict1.items():
        if value not in track:
            track[value] = 0
        else:
            track[value] += 1
    return max(track, key=track.get)


def count(input_list: list[str]) -> dict[str, str]:
    """Count numbers of appearance of each element in the list."""
    result: dict[str, str] = {}
    for i in input_list:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result


def alphabetizer(input_list: list[str]) -> dict[str, list[str]]:
    """Classify each word in the list regarding their first letter."""
    alphabet_dict: dict[str, list[str]] = {}
    for i in input_list:
        if i[0].lower() in alphabet_dict:
            alphabet_dict.get(i[0].lower()).append(i)
        else:
            alphabet_dict[i[0].lower()] = [i]
    return alphabet_dict    


def update_attendance(attendance_record: dict[str, list[str]], weekdays: str, student: str) -> dict[str, list[str]]:
    """Update the attendance log by inserting the name of the student into the provided weekday."""
    if weekdays in attendance_record:
        attendance_record.get(weekdays).append(student)
    else:
        attendance_record[weekdays] = [student]
    return attendance_record