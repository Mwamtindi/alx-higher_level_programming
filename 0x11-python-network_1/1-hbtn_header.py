#!/usr/bin/python3
"""
Script that takes URL as an argument, sends a request to the URL,and
displays the value of the 'X-Request-Id' variable from the response header.
"""

import sys
import urllib.request


def get_x_request_id(url):
    """
    Sends request to the URL and prints X-Request-Id from response header.

    Args:
        url : (str) The URL to send the request to.
    """
    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader('X-Request-Id')
        if x_request_id:
            print(x_request_id)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        get_x_request_id(url)
