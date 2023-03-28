class Node:
    data = None

    def __init__(self, d):
        self.data = d
        self.next = None
    
def append_to_tail(head: Node, d: int):
    end: Node = Node(d)
    n: Node = head
    
    while n.next != None:
        n = n.next
    
    n.next = end

    return head
  
def delete_node(head: Node, d: int):
    n: Node = head

    while n.data != None:
        if n.next.data == d:
            n.next = n.next.next
            return head
        n = n.next
    return head

def print_linked_list(head:Node):
    n: Node = head

    if n.data == None:
        print("None")

    while n != None:
        print(n.data)
        n = n.next

n0 = Node(0)
n1 = Node(1)
n1.next = n0
n2 = Node(2)
n2.next = n1
n3 = Node(3)
n3.next = n2
n4 = Node(4)
n4.next = n3
n5 = Node(5)
n5.next = n4

n5 = append_to_tail(n5,6)
print(print_linked_list(n5))
n5 = delete_node(n5, 3)
print(print_linked_list(n5))
