#!/usr/bin/python3
"""Takes in a letter and sends a POST request"""
if __name__ == "__main__":
    import requests
    import sys
    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': sys.argv[1] if len(sys.argv) > 1 else ""}
    res = requests.post(url, data)
    try:
        if res.json() == {}:
            print("No result")
        else:
            print(f"[{res.json()['id']}] {res.json()['name']}")
    except Exception:
        print("Not a valid JSON")
