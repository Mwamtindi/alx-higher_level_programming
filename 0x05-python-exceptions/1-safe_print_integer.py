#!/usr/bin/python3
def safe_print_integer(value):
    try:
        new-formatted_value = "{:d}".format(value)
        print(new-formatted_value)
        return True
    except (ValueError, TypeError):
        return False

