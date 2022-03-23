'''
Given two (singly) linked lists, determine if the two lists intersect. Return the
intersecting node.  Note that the intersection is defined based on reference, not
 value.   That is, if the kth node of the first linked list is the exact same node
 as the jth node of the second liked list, then they are intersecting.
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

def intersection(llist,llist2):
    llistLen = 1
    llistLen2 = 1
    llistTail = None
    llistTail2 = None
    curr = llist.head

    while curr is not None:
        if curr.next is None:
            llistTail = curr
        llistLen += 1
        curr = curr.next
    curr = llist2.head
    while curr is not None:
        if curr.next is None:
            llistTail2 = curr
        llistLen2 += 1
        curr = curr.next
    if llistTail is not llistTail2:
        return False
    if llistLen < llistLen2:
        shorter = llist.head
        longer = llist2.head
    else:
        longer = llist.head
        shorter = llist2.head
    for i in range(abs(llistLen - llistLen2)):
        longer = longer.next
    while shorter is not longer:
        shorter=shorter.next
        longer = longer.next
    return longer
