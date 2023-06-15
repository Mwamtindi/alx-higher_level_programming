#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_kkeys = sorted(a_dictionary.keys())
    for kkey in sorted_kkeys:
        print(kkey, ":", a_dictionary[kkey])
