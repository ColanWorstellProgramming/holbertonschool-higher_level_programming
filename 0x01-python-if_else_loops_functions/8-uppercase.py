#!/usr/bin/python3
def uppercase(str):
    x = len(str)
    for i in range(0, x):
        if (str[i].islower()):
            c = ord(str[i]) - 32
        else:
            c = str[i]
    if (i != x):
        print("{one}".format(one=chr(c)), end='')
    else:
        print("{one}".format(one=chr(c)))