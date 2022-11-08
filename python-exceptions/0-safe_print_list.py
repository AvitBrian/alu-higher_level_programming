#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    try:
        x =10
        my_list = [1, 2, 3, 4, 5]
        for each in range(x):
            print(f"{my_list[each]}", end="")
        print()
    except:
        print()
