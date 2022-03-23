'''
Implement a function to check if a linked list is a palindrome.
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

def palindrome(llist):
    stack = []
    runner1 = llist.head
    runner2 = llist.head

    while runner2 is not None and runner2.next is not None:
        stack.push(runner1.data)
        runner1 = runner1.next
        runner2 = runner2.next.next

    if runner2 is not None:
        runner1 = runner1.next

    while runner1 is not None:
        temp = stack.pop()
        if runner1.data != temp.data:
            return False
        runner1 = runner1.next
    return True
