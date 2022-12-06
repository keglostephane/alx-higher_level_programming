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
        for line in matrix:
            for value in line:
                if value == line[len(line) - 1]:
                    print("{:d}".format(value))
                else:
                    print("{:d}".format(value), end=' ')
