#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_numerals = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1,
    }

    total = 0
    p = 0
    if roman_string is None or type(roman_string) != str:
        return 0
    for char in roman_string:
        for key, value in roman_numerals.items():
            if char == key:
                if p == 0 or p >= value:
                    total += value
                elif p < value:
                    total += value - (p * 2)
                p = value
    return total
