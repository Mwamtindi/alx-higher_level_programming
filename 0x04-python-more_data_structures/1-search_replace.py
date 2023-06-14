#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for iitem in my_list:
        if iitem == search:
            new_list.append(replace)
        else:
            new_list.append(iitem)
    return new_list
