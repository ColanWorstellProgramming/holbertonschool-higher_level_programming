#!/usr/bin/python3
def uppercase(str):
    x = len(str)
    for i in range(0, x):
        if (str[i].islower()):
            ord(str[i]) = ord(str[i]) - 32
            print(str[i], end='').format()
        else:
            print(str[i], end='').format()
