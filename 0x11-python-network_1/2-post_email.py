#!/usr/bin/python3
"""Makes POST with an email parameter and displays response body in UTF-8"""
if __name__ == "__main__":
    from urllib import request, parse
    import sys
    data = parse.urlencode({'email': sys.argv[2]}).encode()
    with request.urlopen(sys.argv[1], data) as response:
        print(response.read().decode('utf-8'))
