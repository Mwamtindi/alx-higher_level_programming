#!/usr/bin/python3
"""
Script that fetches 'https://alx-intranet.hbtn.io/status' and displays
the body of the response.
"""

import requests


def fetch_status():
    """
    Fetches the status from 'https://alx-intranet.hbtn.io/status' and
    prints the response body details.
    """
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)

    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)


if __name__ == "__main__":
    fetch_status()
