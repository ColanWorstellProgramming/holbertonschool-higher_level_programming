#!/usr/bin/python3
def uppercase(str):
    x = len(str)
    for i in range(0, x):
        if (ord(c) > 96) and (ord(c) < 113):
            if (str[i].islower()):
                c = ord(str[i]) - 32
            else:
                c = str[i]
        if (i != x-1):
            print("{one}".format(one=chr(c)), end='')
        else:
            print("{one}".format(one=chr(c)), end='\n')