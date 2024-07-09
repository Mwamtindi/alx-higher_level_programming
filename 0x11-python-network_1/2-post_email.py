#!/usr/bin/python3
"""
Script that sends a POST request to  URL with email parameter and displays
the body of the response.
"""

import sys
import urllib.parse
import urllib.request


def send_post_request(url, email):
    """
    Sends a POST request to the URL with email as a parameter and prints
    the response body.

    Args:
        url : (str) URL to send the POST request to.
        email : (str) Email to be sent as a parameter.
    """
    data = urllib.parse.urlencode({'email': email}).encode('ascii')

    with urllib.request.urlopen(url, data=data) as response:
        body = response.read().decode('utf-8')
        print(body)


if __name__ == "__main__":
    if len(sys.argv) > 2:
        url = sys.argv[1]
        email = sys.argv[2]
        send_post_request(url, email)
