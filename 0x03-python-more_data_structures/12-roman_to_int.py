#!/usr/bin/python3
def roman_to_int(roman_string):
    i = 0
    ret = 0
    max = len(roman_string)
    x = ""

    if (isinstance(roman_string, str) != True or roman_string == None):
        return(0)

    for i in range(i, max):
        if (i < max):
            if (i+1 < max):
                x = roman_string[i+1]

        if (roman_string[i] == 'C'):
            if (x == 'D'):
                ret += 400
                i += 1
                continue
            if (x == 'M'):
                ret += 900
                i += 1
                continue
            else:
                ret += 100
                continue

        if (roman_string[i] == 'X'):
            if (x == 'L'):
                ret += 40
                i += 1
                continue
            if (x == 'C'):
                ret += 90
                i += 1
                continue
            else:
                ret += 10
                continue

        if (roman_string[i] == 'I'):
            if (x == 'V'):
                ret += 4
                i += 1
                continue
            if (x == 'X'):
                ret += 9
                i += 1
                continue
            else:
                ret += 1
                continue

        if (roman_string[i] == 'V'):
            ret += 5
        if (roman_string[i] == 'L'):
            ret += 50
        if (roman_string[i] == 'D'):
            ret += 500
        if (roman_string[i] == 'M'):
            ret += 1000

    return(ret)
