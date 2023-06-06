#!/usr/bin/python3
for bs in range(0, 10):
    for ms in range(bs + 1, 10):
        if bs == 8 and ms == 9:
            print("{}{}".format(bs, ms))
        else:
            print("{}{}".format(bs, ms), end=', ')
