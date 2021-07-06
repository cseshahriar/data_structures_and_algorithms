""" Single Linked List 
    uses: Operating system design
    uses: graph algorithom
    uses: hash table

    node: [data, next]
    head: start
    next: next data address(pointer)
"""

class Node:
    """ node class """

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        # The repr() function returns a printable representation of the given object.
        return repr(self.data) 
    

class LinkedList:
    """ Linked List """

    def __init__(self):
        # head is None from start
        # data, next also None
        self.head = Node() #node class object 

    def __repr__(self):
        nodes = []
        current_node = self.head.next

        while current_node:
            nodes.append(repr(current_node))
            current_node = current_node.next

        return ",".join(nodes)

    def prepend(self, data):
        """ add item in before first item"""
        node = Node(data, self.head.next)
        self.head.next = node

    def append(self, data):
        """ add item in after last item"""
        node = Node(data) # create node object
        # if linked list is None, then head is None
        # so head.next = node and return
        if self.head.next is None: # if have is empty, than true
            self.head.next = node

            return
        
        # after finish the loop, the last node is current_node
        current_node = self.head.next

        while current_node.next:
            current_node = current_node.next

        # finaly node next is nodes, it's last node
        current_node.next = node
            

    def search(self, item):
        """ search item """
        current_node = self.head.next

        # current_node if None, then loop out
        # else, none's others loop continue  
        while current_node:
            if current_node.data == item:
                return current_node

            current_node = current_node.next

        return None

    def remove(self, item):
        previous_node = self.head
        current_node = previous_node.next

        while current_node:
            if current_node.data == item:
                break

            previous_node = current_node
            current_node = current_node.next
        
        if current_node is None:
            return None
        
        if self.head == previous_node:
            self.head.next = current_node.next
        else:
            previous_node.next = current_node.next

    def insert(self, data, new_data):
        """ insert item between inside first and last"""
        current_node = self.head.next

        while current_node:
            if current_node.data == data:
                new_node = Node(new_data, current_node.next)
                current_node.next = new_node
                break

            current_node = current_node.next
