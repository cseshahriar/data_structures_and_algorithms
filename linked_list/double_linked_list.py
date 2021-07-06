""" Double linked list """

class Node:
    def __init__(self, data=None, prev=None, next=None):
        """ constructor """
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        """ Returns a string as a representation of the object"""
        return repr(self.data)


class DubleLinkedList():
    def __init__(self):
        # head is empty node
        # no node before and after it
        self.head = Node() 

    def __repr__(self):
        nodes = []
        current_node = self.head.next

        while current_node:
            nodes.append(repr(current_node))
            current_node = current_node.next

        return ",".join(nodes)

    def append(self, data):
        node = Node(data)

        if self.head.next is None:
            self.head.next = node
            return
        
        current_node = self.head.next

        while current_node.next:
            current_node = current_node.next
        
        # now current_node next node is node
        # node before node current_node
        current_node.next = node
        node.prev = current_node

    def preprend(self, data):
        # first_node present linkedlist first node maybe
        first_node = self.head.next

        new_node = Node(data, None, first_node)

        self.head.next = new_node

        if first_node:
            first_node.prev = new_node

    def search(self, item):
        current_node = self.head.next
        while current_node:
            if current_node.data == item:
                return current_node

            current_node = current_node.next
        return None

    def remove_node(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head.next = node.next

        if node.next:
            self.next.prev = node.prev

    def remove(self, item):
        node = self.search(item)
        if node is None:
            return

        self.remove_node(node)
        

      

