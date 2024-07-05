#!/usr/bin/python3
"""GitHub API endpoint for listing commits"""
import requests
import sys


if __name__ == "__main__":
    repository = sys.argv[1]
    owner = sys.argv[2]

    url = f'https://api.github.com/repos/{owner}/{repository}/commits'
    params = {
        'per_page': 10,
        'page': 1,
    }

    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            commits = response.json()

            for commit in commits:
                sha = commit['sha']
                author_name = commit['commit']['author']['name']
                print(f"{sha}: {author_name}")
        else:
            print(f"Error: Unable to fetch commits. Status code\
                  {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
