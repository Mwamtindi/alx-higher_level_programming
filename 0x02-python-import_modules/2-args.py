#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    tally = len(sys.argv) - 1
    if tally == 0:
        print("0 arguments.")
    elif tally == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(tally))
    for t in range(tally):
        print("{}: {}".format(t + 1, sys.argv[t + 1]))
