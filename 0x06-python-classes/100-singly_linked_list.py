#!/usr/bin/python3
"""This module provide the following class to work with singly linked list:
* Node: defines a node of a singly linked list
* SinglyLinkedList: defines a singly linked list
"""


class Node:
    """Define a node of a singly linked list.

    :param data: node data
    :type data: int
    :param next_node: next Node
    :type next_node: Node, None
    """

    def __init__(self, data, next_node=None):
        """Initialize a node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get Node data

        :return: the data of the node
        :rtype: int
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data value of the Node.

        :param value: data value of the Node
        :type value: int
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """Get the next Node.

        :return: the next Node object
        :rtype: Node, None
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node.

        :param value: next Node
        :type value: Node, None
        """
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    """Define a singly linked list.
    """
    def __init__(self):
        """Initialise a singly linked list.
        """
        self.__head = []

    def sorted_insert(self, value):
        """inserts a new Node into the correct sorted list.

        :param value: value of the new Node to insert
        :type value: int
        """
        new_node = Node(value)

        if not self.__head:
            self.__head.append(new_node)
        else:
            self.__head[-1].next_node = new_node
            self.__head.append(new_node)

        self.__head.sort(key=lambda node: node.data)

    def __str__(self):
        """Human readable representation of the singly linked list.
        """
        list_as_string = ""

        for node in self.__head:
            if node != self.__head[-1]:
                list_as_string += str(node.data) + "\n"
            else:
                list_as_string += str(node.data)

        return list_as_string
