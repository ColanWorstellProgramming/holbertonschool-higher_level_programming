#!/usr/bin/python3
x = 1
for i in range(0, 10):
    for x in range(i+1, 10):
        print(i, x.format())
    x = x + 1
