#!/usr/bin/python3
def pow(a, b):
    if b == 0 and a == 0:
        return 0
    elif b == 0:
        return 1
    else:
        return a ** b
