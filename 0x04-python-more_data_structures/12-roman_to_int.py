#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    roman_dictn = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    rom= [roman_dictn[x] for x in roman_string]
    output = 0
    for i in range(len(rom)):
        output += rom[i]
        if rom[i - 1] < rom[i] and i != 0:
            output -= (rom[i - 1] + rom[i - 1])
    return output
