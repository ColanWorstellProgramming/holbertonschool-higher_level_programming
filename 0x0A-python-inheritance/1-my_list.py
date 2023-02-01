#!/usr/bin/python3
"""MyList class file"""


class MyList(list):
    """function in class to print sorted list"""
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
