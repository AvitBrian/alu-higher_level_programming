#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    ret = 0
    for y in range(x):
        try:
            if str(my_list[y]).isdigit():
                print("{:d}".format(my_list[y]), end ="")         
                ret += 1
        except IndexError:
            continue
    print()
    return ret
