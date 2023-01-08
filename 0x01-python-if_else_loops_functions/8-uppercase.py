#!/usr/bin/python3
def uppercase(str):
    x = len(str)
    for i in range(0, x):
        if (ord(str[i]) > 96) and (ord(str[i]) < 113):
            c = ord(str[i]) - 32
        else:
            c = str[i]
        if (i != x-1):
            print("{one}".format(one=chr(c)), end='')
        else:
            print("{one}".format(one=chr(c)), end='\n')