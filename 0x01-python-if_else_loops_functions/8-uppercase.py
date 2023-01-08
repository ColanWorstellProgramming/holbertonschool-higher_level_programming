#!/usr/bin/python3
def uppercase(str):
    x = len(str)
    for i in range(0, x):
        if ((ord(str[i]) > 96) and (ord(str[i]) < 113)):
            c = chr(ord(str[i]) - 32)
        print("{one}".format(one=c), end='')
    print("")
