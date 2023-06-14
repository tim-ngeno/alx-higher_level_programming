#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_numerals = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    total = 0
    for char in roman_string:
        for key, value in roman_numerals.items():
            if char == key:
                total += value
    return total
