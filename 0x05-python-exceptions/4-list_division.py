#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element 2 lists.

    :param my_list_1: first list
    :type my_list_1: list
    :param my_list_2: second list
    :type my_list_2: list
    :return: a new list with all divisions and length = `list_length`
    :rtype: list
    """
    new_list = []
    for i in range(list_length):
        try:
            new_list.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except TypeError:
            print("wrong type")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
        finally:
            pass

    return new_list
