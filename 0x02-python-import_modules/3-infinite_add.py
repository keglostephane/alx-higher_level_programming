#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    args = len(argv)
    sum = 0

    if args == 1:
        print(sum)
    else:
        for i in range(1, args):
            sum += int(argv[i])
        print(sum)
