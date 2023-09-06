#!/usr/bin/python3
"""Using Github API, displays user id"""

if __name__ == "__main__":
    import requests
    import sys
    username = sys.argv[1]
    access_token = sys.argv[2]
    url = 'https://api.github.com/user'
    req = requests.get(url, auth=(username, access_token))
    print(req.json().get('id'))
