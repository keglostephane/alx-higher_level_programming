#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    names = dir(hidden_4)
    for i in range(len(names)):
        if not names[i].startswith('_'):
            print("{}".format(names[i]))
