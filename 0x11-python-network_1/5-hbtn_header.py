#!/usr/bin/python3
"""Displays X-Request-Id variable found in the header of a URL response"""
if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    res = requests.get(url)
    print(res.headers.get('X-Request-Id'))
