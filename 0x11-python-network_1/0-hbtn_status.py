#!/usr/bin/python3
"""
This module fetches the status from 'https://alx-intranet.hbtn.io/status'
using the 'urllib' package and displays the response body.
"""

import urllib.request


def fetch_status():
    """
    Fetches the status from 'https://alx-intranet.hbtn.io/status'
    and prints the response body details.
    """
    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
        print("\t- utf8 content:", body.decode('utf-8'))


if __name__ == "__main__":
    fetch_status()
