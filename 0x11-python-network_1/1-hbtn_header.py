#!/usr/bin/python3
"""Write a python script that takes in a URL, sends a request
and display the value of the x-Request_Id variable of the header"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        headers = response.getheaders()
        x_request_id = dict(headers).get("X-Request-Id")

    if x_request_id:
        print(x_request_id)
