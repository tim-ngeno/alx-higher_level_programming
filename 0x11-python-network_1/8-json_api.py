#!/usr/bin/python3
"""
Write ascript that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    url = "http://0.0.0.0:5000/search_user"
    value = {"q": q}
    res = requests.post(url, data=value)

    try:
        json_res = res.json()
        if json_res:
            print("[{}] {}".format(json_res.get("id"),
                                   json_res.get("name")))
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
