#!/bin/bash
# A script that takes URL sends POST request to the passed URL and displays bdy
curl -s -X POST -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" "$1"
