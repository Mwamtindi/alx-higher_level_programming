#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_numb = set()
    tot_sum = 0
    for nnum in my_list:
        if nnum not in unique_numb:
            unique_numb.add(nnum)
            tot_sum += nnum
    return tot_sum
