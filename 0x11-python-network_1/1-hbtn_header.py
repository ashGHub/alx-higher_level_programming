#!/usr/bin/python3
"""Displays X-Request-Id variable found in the header of a URL response"""

if __name__ == "__main__":
    from urllib import request
    import sys
    url = sys.argv[1]
    with request.urlopen(url) as response:
        print(response.headers.get('X-Request-Id'))
