#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i == 8 and j > i:
            print("{}{}".format(i, j))
        elif i != j and i < j:
            print("{}{},".format(i, j), end=' ')
