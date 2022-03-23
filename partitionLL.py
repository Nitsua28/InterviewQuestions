'''
Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. If x is contained within the list, the values of x
only need to be after the elements less than x (see below). The partition element x can appear
anywhere in the "right partition"; it does not need to appear between the left and right partitions
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


def partition(llist, x):
    temp1 = LinkedList()
    curr = llist.head
    while curr is not None:
        if curr.data < x:
            temp1.push_back(Node(curr.data))
        curr = curr.next
    curr = llist.head

    while curr is not None:
        if curr.data >= x:
            temp1.push_back(Node(curr.data))
        curr = curr.next
    return temp1

llist = LinkedList()
llist.head = Node(4)
llist.push_back(Node(3))
llist.push_back(Node(2))
llist.push_back(Node(1))
llist.display()
temp = partition(llist,2)
temp.display()
