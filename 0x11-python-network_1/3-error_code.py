#!/usr/bin/python3
"""Makes a request and displays response body in UTF-8"""
if __name__ == "__main__":
    from urllib import request, error
    import sys
    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
