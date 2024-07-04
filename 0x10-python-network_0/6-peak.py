#!/usr/bin/python3
"""
peak_finder.py file

A module to find a peak in a list of unsorted integers using binary search.
"""

def find_peak(list_of_integers):
    """
    Fxn that finds peak in list of unsorted integers using binary search.

    Args:
    - list_of_integers (list): list of unsorted integers.

    Returns:
    - int: peak element from the list.
    """
    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]
