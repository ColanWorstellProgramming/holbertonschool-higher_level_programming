#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ((ord(char) > 96) and (ord(char) < 113)):
            char = chr(ord(str[i]) - 32)
        print("{one}".format(one=char), end='')
    print("")
