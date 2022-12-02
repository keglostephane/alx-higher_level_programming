#!/usr/bin/python3
import sys
if __name__ == "__main__":
    print("{} argumen{}{}".format(len(sys.argv) - 1,
          't' if len(sys.argv) == 2 else "ts",
          '.' if len(sys.argv) == 1 else ':'))

    if (len(sys.argv) >= 2):
        for i in range(len(sys.argv)):
            if i != 0:
                print("{}: {}".format(i, sys.argv[i]))
