#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""
if __name__ == "__main__":
    import requests
    res = None
    try:
        res = requests.get("http://0.0.0.0:5050/status")
    except Exception as e:
        res = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print(f"\t- type: {type(res.text)}")
    print(f"\t- content: {res.text}")
