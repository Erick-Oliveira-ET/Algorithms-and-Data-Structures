from typing import Optional


class Node:
    def __init__(self, d: int):
        self.data: int = d
        self.next: Optional[Node] = None

"""
  Write code to remove duplicates from an unsorted linked list.

  Follow up: How would you solve this problem if a temporary buffer is not allowed?
"""

def remove_dups(head: Node):
    n = head

    if n == None and n.data != None:
        return head
    
    set_data = set()
    set_data.add(n.data)

    while n.next != None and n.next.data != None:
        if n.data not in set_data:
            set_data.add(n.data)
        
        temp = n

        while temp.next != None and temp.next.data in set_data:
            temp = temp.next

        n.next = temp.next
        n = n.next

    
    return head

def print_linked_list(head:Node):
    n: Node = head
    temp_list = []

    if n.data == None:
        print("None")
        return

    while n != None:
        temp_list.append(str(n.data))
        n = n.next
    
    temp_list.append(str(None))
    print(" -> ".join(temp_list))

n0 = Node(0)
n1 = Node(1)
n1.next = n0
n2 = Node(3)
n2.next = n1
n3 = Node(3)
n3.next = n2
n4 = Node(4)
n4.next = n3
n5 = Node(4)
n5.next = n4

print_linked_list(n5)
n5 = remove_dups(n5)
print_linked_list(n5)