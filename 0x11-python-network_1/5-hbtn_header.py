#!/usr/bin/python3
"""Displays X-Request-Id variable found in the header of a URL response"""
if __name__ == "__main__":
    import requests
    import sys
    res = requests.get(sys.argv[1])
    print(res.headers.get('X-Request-Id'))
