#!/usr/bin/python3
def remove_char_at(str, n):
    length = len(str)
    if n < 0 or n >= length:
        return str
    if not n:
        return str[1:]
    if n == length - 1:
        return str[:-1]
    return str[:n] + str[n+1:]
