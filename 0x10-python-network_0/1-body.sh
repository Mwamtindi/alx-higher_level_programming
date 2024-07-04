#!/bin/bash
# A script that takes in URL, sends a GET request to URL, and displays the body
curl -s -w "%{http_code}\n" "$1" | grep -q "200" && curl -s "$1"
