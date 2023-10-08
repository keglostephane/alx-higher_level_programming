#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is not None:
        return [True if num % 2 == 0 else False for num in my_list]
