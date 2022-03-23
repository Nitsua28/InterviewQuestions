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
    # def remove(self, key):
    # 	if self.head == None:
    #   	return
    # 	temp = self.head
    #   prev = None
    # 	while temp.next is not None:
    #   	while temp.data is not key:
    #     	temp = temp.next
    #       prev = temp
    #     prev.next = temp.next
    #     temp = prev.next
    # def push_back(self,node):
  	#     if self.head == None:
    # 	   self.head = node
    # 	   return
    #
  	#     temp = self.head
    #
    #     while temp.next is not None:
    #        temp = temp.next
    #
    #     temp.next = node

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
Remove Dups: Write code to remove duplicates from an unsorted linked list.
using buffer

O(n) runtime
O(n) space
'''
#using buffer
def removeDup(llist):
    hash = {}
    curr = llist.head
    while curr is not None:
        if curr.data in hash:
            llist.remove(curr.data)
        else:
            hash[curr.data] = 1
        curr = curr.next
'''
empty list
'''
llist = LinkedList()

llist.display()

removeDup(llist)

llist.display()
