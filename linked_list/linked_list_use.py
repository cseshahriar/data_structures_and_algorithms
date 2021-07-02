from linked_list import *

print('Hello')

ll = LinkedList()
ll.append(5)
ll.append(10)
print('8: ', ll)

ll.prepend(1)
print('11: ', ll) # first insert

search_val = ll.search(5)
print('14: ', search_val)

ll.append(50)
print('17 ', ll)

ll.remove(50)
print('18: ', ll)

ll.insert(5,6)
ll.remove(1)
print('22: ', ll)
