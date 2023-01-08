#!/usr/bin/python3
def uppercase(str):
    x = len(str)
    for i in range(0, x):
        if (str[i].islower()):
            c = ord(str[i]) - 32
            print("{one}".format(one=c), end='')
        else:
            print("{one}".format(one=str[i]), end='')
