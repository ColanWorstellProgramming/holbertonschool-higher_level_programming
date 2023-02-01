#!/usr/bin/python3
"""json file"""
import sys
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    """compare"""
    try:
        load_this = load("add_item.json")
    except FileNotFoundError:
        load_this = []
    load_this.extend(sys.argv[1:])
    save(load_this, "add_item.json")