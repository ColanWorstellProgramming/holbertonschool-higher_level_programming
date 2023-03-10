#!/usr/bin/python3
"""HBTN Status"""
import requests


if __name__ == "__main__":
    req = requests.Request('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))
