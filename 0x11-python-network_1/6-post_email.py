#!/usr/bin/python3
"""Makes POST with an email parameter and displays response body in UTF-8"""
if __name__ == "__main__":
    import requests
    import sys
    res = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(res.text)
