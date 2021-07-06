from double_linked_list import *

def test_appent():
    dll = DubleLinkedList()
    assert dll.head.next == None, "linked list empty, so head should point to None"  # noqa
    
    item = 5
    dll.append(item)
    assert dll.head.next.data == item, "head should point to the first item node"
    
    second_item = 8
    dll.append(second_item)
    assert dll.head.next.data == item, "head should point to first item node"

    first_node = dll.head.next
    second_node = first_node.next
    assert first_node.data == second_item, "first node should point to second"

    assert second_node.prev.data == item, "previous node of second_node should point to first node"

    assert str(dll) == "5,8", "string representation of dll should match 5,8"

