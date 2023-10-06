#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    from sys import argv, exit

    args = len(argv)
    op = ("+", "-", "*", "/")

    if args != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)
    elif args == 4 and argv[2] not in op:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    elif args == 4 and argv[2] in op:
        if argv[2] == "+":
            print("{} + {} = {:d}".format(argv[1], argv[3],
                                          add(int(argv[1]), int(argv[3]))))
        if argv[2] == "-":
            print("{} - {} = {:d}".format(argv[1], argv[3],
                                          sub(int(argv[1]), int(argv[3]))))
        if argv[2] == "*":
            print("{} * {} = {:d}".format(argv[1], argv[3],
                                          mul(int(argv[1]), int(argv[3]))))
        if argv[2] == "/":
            print("{} / {} = {:d}".format(argv[1], argv[3],
                                          div(int(argv[1]), int(argv[3]))))
