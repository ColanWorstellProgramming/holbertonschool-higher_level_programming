#!/usr/bin/python3
def no_c(my_string):
    text = my_string
    for i in range(0, len(my_string)):
        if (ord(my_string[i]) == 67 or ord(my_string[i]) == 99):
            text = text[0:i] + text[i+1:]
    my_string = text
    return my_string
