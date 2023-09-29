#!/usr/bin/python3
"""
Using urllib to perform a GET request
"""

import urllib.request

if __name__ == "__main__":
    hbtn_url = urllib.request.Request("https://alx-intranet.hbtn.io/status")

    with urllib.request.urlopen(hbtn_url) as req:
        res = req.read()
        print("Body response:")
        print("\t- type: {}".format(type(res)))
        print("\t- content: {}".format(res))
        print("\t- utf8 content: {}".format(res.decode('UTF-8')))
