#!/usr/bin/python3
def no_c(my_string):
    if my_string is not None:
        new_string = ""
        for ch in my_string:
            if ch not in "cC":
                new_string += ch
        return new_string
