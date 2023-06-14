#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_sset = set()
    for eelement in set_1:
        if eelement in set_2:
            common_sset.add(eelement)
    return common_sset
