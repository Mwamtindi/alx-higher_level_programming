#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    tally = []
    for numb in my_list:
        tally.append(numb % 2 == 0)
    return tally
