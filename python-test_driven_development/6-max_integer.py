#!/usr/bin/python3
""" creats a function that finds the max int """

def max_integer(list=[]):
    """ finds the max insteger """
    if len(list) == 0:
        return None
    res = list[0]
    a = 1
    while a < len(list):
        if list[i] > res:
            res = list[i]
        a += 1
    return res
