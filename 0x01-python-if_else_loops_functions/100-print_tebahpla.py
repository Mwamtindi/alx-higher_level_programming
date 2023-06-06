#!/usr/bin/python3
for revs in range(26):
    if revs % 2 == 0:
        print('{:c}'.format(122 - revs), end='')
    else:
        print('{:c}'.format(90 - revs), end='')
