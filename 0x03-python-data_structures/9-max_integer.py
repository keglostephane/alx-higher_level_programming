#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is not None:
        if not my_list:
            return None
        else:
            max = my_list[0]
            for num in my_list:
                if num > max:
                    max = num
            return max
