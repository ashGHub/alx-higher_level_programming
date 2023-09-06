#!/usr/bin/python3
"""Script to fetch https://intranet.hbtn.io/status"""


def print_response(res):
    """Prints the response of a URL request"""
    html = res.read()
    print("Body response:")
    print(f"\t- type: {type(html)}")
    print(f"\t- content: {html}")
    print(f"\t- utf8 content: {html.decode('utf-8')}")


if __name__ == "__main__":
    from urllib import request
    try:
        with request.urlopen('http://0.0.0.0:5050/status') as response:
            print_response(response)
    except Exception as e:
        with request.urlopen('https://intranet.hbtn.io/status') as response:
            print_response(response)
