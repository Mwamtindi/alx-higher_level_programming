#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff_sset = set()
    for eelement in set_1:
        if eelement not in set_2:
            diff_sset.add(eelement)
    for eelement in set_2:
        if eelement not in set_1:
            diff_sset.add(eelement)
    return diff_sset
