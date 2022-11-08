#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    ret = 0
    for each in range(x):
        try:
            print(f"{my_list[each]}", end="")
            ret += 1
        except:
            break
    print()
    return (ret)
