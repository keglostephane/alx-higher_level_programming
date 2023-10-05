#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    args = len(argv)

    print("{:d} argument{}{}".format(args - 1, "s" if args != 2 else "",
                                     ":" if args >= 2 else "."))

    for i in range(1, args):
        print("{:d}: {}".format(i, argv[i]))
