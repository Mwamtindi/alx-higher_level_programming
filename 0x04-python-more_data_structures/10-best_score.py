#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_kkey = None
    max_vvalue = float('-inf')
    for key, value in a_dictionary.items():
        if value > max_vvalue:
            max_kkey = key
            max_vvalue = value
    return max_kkey
