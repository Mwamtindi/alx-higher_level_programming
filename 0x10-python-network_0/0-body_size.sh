#!/bin/bash
# A script that takes in a URL, sends a request to URL, and display the size.
curl -s "$1" | wc -c
