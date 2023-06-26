#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    tal = 0
    try:
        for l in my_list[:x]:
            try:
                print("{:d}".format(l), end=" ")
                tal += 1
            except (ValueError, TypeError):
                pass
    except IndexError:
        pass
    
    print()
    return tal
