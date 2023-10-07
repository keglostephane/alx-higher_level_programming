#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a is not None and tuple_b is not None:
        new_tuple = ()
        sum = 0
        for i in range(2):
            try:
                sum += tuple_a[i]
            except IndexError:
                sum += 0
            try:
                sum += tuple_b[i]
            except IndexError:
                sum += 0
            new_tuple += sum,
            sum = 0
        return new_tuple
