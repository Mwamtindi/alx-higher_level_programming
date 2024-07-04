#!/bin/bash
# A bash script that takes in a URL, sends a request to URL, and display
# +the size of the body of the response.
curl -s "$1" | wc -c
