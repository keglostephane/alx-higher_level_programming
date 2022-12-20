#!/usr/bin/python3
65;6800;1cdef safe_print_list(my_list=[], x=0):
    """Prints `x` elements of a list.

    Args:
    my_list (list) : a list
    x (int) : number of elements to print

    Returns:
    (int) : the real number of elements printed
    """
    if my_list == [] or x < 0:
        print(None)
        return None
    else:
        try:
            for i in range(x):
                print(f"{my_list[i]}", end='')
            print("")
            return i + 1
        except IndexError:
            print("")
            return i
