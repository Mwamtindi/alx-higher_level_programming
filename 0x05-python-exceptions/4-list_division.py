#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    neww_list = []
    for u in range(list_length):
        try:
            res = my_list_1[u] / my_list_2[u]
        except (ValueError, TypeError):
            print("wrong type")
            res = 0
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        except IndexError:
            print("out of range")
            res = 0
        finally:
            neww_list.append(res)
    return neww_list
