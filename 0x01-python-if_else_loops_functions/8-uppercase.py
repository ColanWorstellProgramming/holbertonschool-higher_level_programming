#!/usr/bin/python3
def uppercase(str):
    x = len(str)
    for i in range(0, x):
        if (str[i].islower()):
            str[i] = str[i] - 32
        print(str[i], end='')