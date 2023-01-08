#!/usr/bin/python3
def uppercase(str):
    x = len(str)
    for i in range(0, x):
        if (str[i].islower()):
            c = ord(str[i]) - 32
            print("{one}", end='').format(one=c)
        else:
            print("{one}", end='').format(one=str[i])
