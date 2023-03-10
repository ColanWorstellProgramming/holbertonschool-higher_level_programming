#!/usr/bin/python3
"""HBTN Status"""
import requests, sys


if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    print(req.headers['X-Request-Id'])

