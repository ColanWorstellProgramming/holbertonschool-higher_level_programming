#!/usr/bin/python3
"""json file"""
import json


def to_json_string(my_obj, filename):
    """json"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
