#!/usr/bin/python3
"""Using Github API, displays 10 commits of given repo and user"""
if __name__ == "__main__":
    import requests
    import sys
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'
    req = requests.get(url)
    # get first 10 commits
    for commit in req.json()[0:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
