#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list is not None:
        length = len(my_list)
        if idx < 0 or idx >= length:
            return my_list
        else:
            del my_list[idx]
            return my_list
