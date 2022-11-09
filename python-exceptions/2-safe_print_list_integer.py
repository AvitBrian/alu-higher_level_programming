#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    for y in range(x+1):
        try:
            if str(my_list[y]).isdigit():
                print("{:d}".format(my_list[y]), end ="")         
        except IndexError:
            print("List out  of range")
    print()
