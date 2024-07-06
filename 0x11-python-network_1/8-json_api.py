#!/usr/bin/python3
"""Takes in a letter and sens a POST request to
http://0.0.0.0:5000/search_user with letter as a parameter"""
import requests
import sys

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""

    payload = {'q': letter}
    url = 'http://0.0.0.0:5000/search_user'

    try:
        response = requests.post(url, data=payload)
        json_data = response.json()

        if json_data:
            print(f"[{json_data.get('id')}] {json_data.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
