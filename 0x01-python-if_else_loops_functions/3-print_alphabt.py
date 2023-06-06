#!/usr/bin/python3
for lowt in range(97, 123):
    if chr(lowt) not in ['q', 'e']:
        print('{}'.format(chr(lowt)), end='')
