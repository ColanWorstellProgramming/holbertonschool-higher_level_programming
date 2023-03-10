#!/usr/bin/python3
"""HBTN Status"""
from urllib import request, pasrse
import sys

if __name__ == "__main__":
    req = request.Request(sys.argv[1], sys.argv[2])
    with request.urlopen(req) as response:
        html = response.read()
        print(response.headers['X-Request-Id'])
