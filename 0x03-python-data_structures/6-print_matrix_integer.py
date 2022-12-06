#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers.

    Args:
    matrix (list) : list of integers list

    Returns:
    None
    """
    if matrix == [[]]:
        print("")
    else:
        for l in matrix:
            for e in l:
                if e == l[len(l) - 1]:
                    print("{:d}".format(e))
                else:
                    print("{:d}".format(e), end=' ')
