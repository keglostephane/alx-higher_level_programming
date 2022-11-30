#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return str
    else:
        new_str = ""
        for c in str:
            if str[n] != c:
                new_str += c
        return new_str
