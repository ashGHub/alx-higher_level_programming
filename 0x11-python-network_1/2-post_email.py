#!/usr/bin/python3
"""Makes POST with an email parameter and displays response body in UTF-8"""
if __name__ == "__main__":
    from urllib import request, parse
    import sys
    url = sys.argv[1]
    email = sys.argv[2]
    data = parse.urlencode({'email': email}).encode()
    with request.urlopen(url, data) as response:
        print(response.read().decode('utf-8'))
