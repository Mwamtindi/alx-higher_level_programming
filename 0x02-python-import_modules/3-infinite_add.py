#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    tsum = 0
    for v in argv[1:]:
        tsum += int(v)
    print("{:d}".format(tsum))
