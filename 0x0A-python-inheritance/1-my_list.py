#!/usr/bin/python3
"""MYList class file"""


class MyList(list):
    """function in class to print sorted list"""
    def print_sorted(self):
        print(sorted(self))
