#!/usr/bin/python3
"""A class Node of a singly linked list"""


class Node:
    """Defines the node of a singly linked list

    Attributes:
        data: data item for the node
        next_node: link to the next node in the list
    """

    def __init__(self, data, next_node=None):
        """Initializes the linked list
        Args:
            data: data part of the node
            next_node: holds the address of the next node
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Getter/Setter properties for the data part of the node"""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter and setter for the address part of the node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if (value is not None) and (not isinstance(value, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list class

    Attributes:
        head: the head node of the singly linked list
    """

    def __init__(self):
        """Initializes the SinglyLinkedList list"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new node Node in correct sorted position
        Args:
            value (Node): new node
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            while (temp.next_node is not None and
                   temp.next_node.data < value):
                temp = temp.next_node
            new.next_node = temp.next_node
            temp.next_node = new

    def __repr__(self):
        items = []
        temp = self.__head
        while temp is not None:
            items.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(items))
