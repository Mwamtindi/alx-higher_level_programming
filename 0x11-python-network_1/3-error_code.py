#!/usr/bin/python3
"""
Script that sends request to a URL and displays the body of the response.
It also handles HTTPError exceptions and displays error code if one occurs.
"""

import sys
import urllib.request
import urllib.error


def fetch_url(url):
    """
    Sends request to given URL and prints the body of the response.
    If an HTTPError occurs, it prints the error code.

    Args:
        url : (str) URL to send the request to.
    """
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        fetch_url(url)
