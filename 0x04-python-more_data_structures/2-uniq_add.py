#!/usr/bin/python3
def uniq_add(my_list=[]):
    list_uniq = set(my_list)
    calc = 0
    for i in list_uniq:
        calc += i

    return (calc)
