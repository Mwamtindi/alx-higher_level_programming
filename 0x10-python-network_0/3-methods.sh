#!/bin/bash
# A script that takes URL and displays all HTTP methods the server will accept
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d ' ' -f2-
