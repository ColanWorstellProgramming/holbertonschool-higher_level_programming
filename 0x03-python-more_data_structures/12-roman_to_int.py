#!/usr/bin/python3
def roman_to_int(roman_string):
    val = {'I':1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    var = 0

    if (isinstance(roman_string, str) != True or roman_string == None):
        return(0)

    for i in range(len(roman_string)):
        if i+1 < len(roman_string) and val[roman_string[i]] < val[roman_string[i+1]]:
            var -= val[roman_string[i]]
        else:
            var += val[roman_string[i]]
    return (var)
