#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    ttotal_weight = 0
    weighted_sum = 0
    for tup, weight in my_list:
        ttotal_weight += weight
        weighted_sum += tup * weight
    return weighted_sum / ttotal_weight
