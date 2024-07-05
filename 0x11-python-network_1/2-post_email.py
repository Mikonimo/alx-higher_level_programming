#!/usr/bin/python3
"""Takes in a URL and an email, seds a POST request to the passed URL with
the email as a parameterl"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    with urllib.request.urlopen(url, data) as response:
        body = response.read().decode('utf-8')

    print(body)
