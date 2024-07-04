#!/bin/bash
# A script that takes in URL, sends a GET request to URL, and displays the body
curl -s -o /dev/stderr -w "%{http_code}" "$1"
