#!/usr/bin/python3
"""Makes POST with an email parameter and displays response body"""
if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    email = sys.argv[2]
    res = requests.post(url, data={'email': email})
    print(res.text)
