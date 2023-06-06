#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        rmdst = str[:n] + str[n + 1:]
        return (rmdst)
    else:
        return (str)
