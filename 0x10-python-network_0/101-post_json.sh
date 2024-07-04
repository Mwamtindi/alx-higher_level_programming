#!/bin/bash
# Script that sends JSON POST request t URL passed as first arg & displays body
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
