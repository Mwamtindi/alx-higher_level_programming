#!/bin/bash
# A script that sends DELETE request passed as first arg and displays the body
curl -s -X DELETE "$1"
