class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

def kth_element(head, k):
    n = head

    for _ in range(k - 1):
        if n.next == None:
            n.data = None
            break
        n = n.next
    
    return n.data

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

print(kth_element(n5, 3))
print(kth_element(n5, 5))
print(kth_element(n5, 7))
print(kth_element(n5, 8))