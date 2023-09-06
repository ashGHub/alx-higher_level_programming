#!/usr/bin/python3
"""Using Github API, displays user id"""

if __name__ == "__main__":
    import requests
    import sys
    url = 'https://api.github.com/user'
    req = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    print(req.json().get('id'))
