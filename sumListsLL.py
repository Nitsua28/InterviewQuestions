'''
You have two numbers represented by a linked list, where each node contains a single digit.
  The digits are stored in reverse order, such that the 1's digit is at the head of the list.
  Write a function that adds the two numbers and returns the sum as a linked list.
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

    def push_front(self,node):
        if self.head != None:
            nextNode = self.head
            self.head = node
            node.next = nextNode
        else:
            self.head = node
    # def push_front(self,node):
    # 	if self.head != None:
    #   	nextNode = self.head #previous head is now next
    #     self.head = node #new head is node
    #     node.next = nextNode
    #   else:
    #   	self.head = node

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

def sumLists(llist1,llist2):
    str1 = ""
    str2 = ""
    temp = LinkedList()
    curr = llist1.head
    while curr is not None:
        str1 += str(curr.data)
        curr = curr.next
    curr = llist2.head
    while curr is not None:
        str2 += str(curr.data)
        curr = curr.next
    sum = int(str1) + int(str2)
    strTemp = str(sum)
    for i in strTemp:
        temp.push_front(Node(i))
    return temp
'''
runtime : O(n) length of the longer llist
spacetime : O(n) based on length of the longer llist
'''
str1 = LinkedList()
str1.push_back(Node(4))
str1.push_back(Node(3))
str1.push_back(Node(3))
str2 = LinkedList()
str2.push_back(Node(2))
str2.push_back(Node(4))
str2.push_back(Node(3))
sumLists(str1,str2).display()
