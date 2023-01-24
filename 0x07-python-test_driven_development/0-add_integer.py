#!/usr/bin/python3
def add_integer(a, b=98):
    if (a is not int or float):
        raise TypeError('a must be an integer')
    elif (b is not int or float):
        raise TypeError('b must be an integer')

    if (b is float):
        b = int(b)
    if (a is float):
        a = int(a)

    return a + b