'''
Implement an algorithm to find the kth to last element of a singly linked list
'''
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    def push_back(self,node):
        if self.head == None:
            self.head = node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = node

    def remove(self, key):
        if self.head == None:
            return
        temp = self.head
        prev = None
        while temp.next is not None:
            while temp.data is not key:
                prev = temp
                temp = temp.next
            prev.next = temp.next
            temp = prev.next

    def display(self):
        if self.head is None:
            print("Empty")
            return
        print(self.head.data, end = "")
        curr = self.head
        while curr.next is not None:
            print("->", end = "")
            curr = curr.next
            print(curr.data, end = "")
        print()
'''
2 pointer, runner method
'''

def kthToLast(llist,k):
    first = llist.head
    second = llist.head

    for i in range(k):
        if second is None:
            print("out of range")
            return
        second = second.next
    while second is not None:
        second = second.next
        first = first.next
    return first.data

'''
O(n) runtime
O(1) space

Constraints
 0 < len(llist) < 999
 0 < k < 999
'''

'''
Regular
'''
print("regular")

llist = LinkedList()
llist.push_back(Node(1))
llist.push_back(Node(2))
llist.push_back(Node(3))
llist.push_back(Node(4))
llist.display()
print(kthToLast(llist,3))

'''
extremes
'''
print("extremes")

llist2 = LinkedList()

llist2.display()
print(kthToLast(llist2,3))

'''
'''
