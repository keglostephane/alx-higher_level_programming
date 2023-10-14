#!/usr/bin/python3

def roman_to_int(roman_string):
    """Convert a Roman numeral to an integer.

    :param roman_string: a Roman numeral
    :type roman_string: str
    :return: an integer value of the Roman numeral.
        If the roman_string is not a string or None, return 0
    :rtype: int
    """
    if roman_string is None or type(roman_string) is not str:
        return 0

    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                 'M': 1000}
    result = 0
    prev = 0
    for ch in roman_string:
        value = roman_map[ch]
        if prev < value:
            if not prev:
                result = value
            else:
                result -= prev
                result += value - prev
        else:
            result += value
        prev = value
    return result
