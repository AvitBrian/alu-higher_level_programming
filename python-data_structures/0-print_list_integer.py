#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for each in my_list:
        print("{:d}".format(my_list[each - 1]))
