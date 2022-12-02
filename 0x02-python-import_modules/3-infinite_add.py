#!/usr/bin/python3
import sys

if __name__ == "__main__":
    sum = 0
    if len(sys.argv) == 1:
        print("{}".format(0))
    else:
        for i in range(len(sys.argv)):
            if i != 0:
                sum += int(sys.argv[i])
        print("{}".format(sum))
