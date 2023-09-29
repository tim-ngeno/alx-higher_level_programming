#!/usr/bin/python3
"""Fetch Github commits from repository `rails` by the user `rails`
"""
import requests
import sys

if __name__ == "__main__":

    repo = sys.argv[1]
    owner = sys.argv[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(
        owner, repo
    )

    res = requests.get(url)
    as_json = res.json()

    for item in as_json[:10]:
        print("{}: {}".format(item["sha"], item["commit"]["author"]["name"]))
