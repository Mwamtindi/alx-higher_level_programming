#!/bin/bash
# makes req to '0.0.0.0:5000/catch_me' causes the server respond with message
curl -s -X PUT 0.0.0.0:5000/catch_me
