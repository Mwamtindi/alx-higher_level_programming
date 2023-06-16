#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_to_delete = []
    for kkey, vall in a_dictionary.items():
        if vall == value:
            keys_to_delete.append(kkey)
    for kkey in keys_to_delete:
        del a_dictionary[kkey]
    return a_dictionary
