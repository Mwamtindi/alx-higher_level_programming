#!/bin/bash
# Script that sends request t URL passes as arg, and displays only status code
curl -s -o /dev/null -w "%{http_code}" "$1"
