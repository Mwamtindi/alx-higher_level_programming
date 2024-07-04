#!/bin/bash
# A script that takes in URL, sends a GET request to URL, and displays the body
if [ "$(curl -s -o /dev/null -w '%{http_code}' "$1")" -eq 200 ]; then curl -s "$1"; fi
