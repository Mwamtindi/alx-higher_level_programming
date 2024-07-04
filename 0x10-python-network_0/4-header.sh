#!/bin/bash
# A script that takes URL as arg, sends GET request and displays the body.
curl -s -H "X-School-User-Id: 98" "$1"
