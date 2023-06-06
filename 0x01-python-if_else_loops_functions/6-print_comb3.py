#!/usr/bin/python3
for bs in range(0, 8):
    for ms in range(bs + 1, 10):
        print("{:d}{:d}".format(bs, ms), end=', ')
        print("{:d}{:d}".format(bs + 1, ms))
