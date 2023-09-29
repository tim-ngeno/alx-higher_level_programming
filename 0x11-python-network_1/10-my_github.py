#!/usr/bin/python3
"""Using the GitHub API endpoint to display my ID"""

import requests
import sys
from requests.auth import HTTPBasicAuth
if __name__ == "__main__":

    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"

    auth = HTTPBasicAuth(username, token)

    res = requests.get(url, auth=auth)

    print(res.json().get("id"))
