#!/usr/bin/python3
def uppercase(str):
    for c in str:
        print("{}".format(c if ord(c) < 97 or ord(c) > 122
                          else chr(ord(c) - 32)), end="")
    print()
