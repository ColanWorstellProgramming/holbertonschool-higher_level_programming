#!/usr/bin/python3
"""HBTN Status"""
import urllib.request
import sys

if __name__ == "__main__":
    req = urllib.request.Request('https://intranet.hbtn.io')
    with urllib.request.urlopen(req) as response:
        html = response.read()
        print(response.headers['X-Request-Id'])
