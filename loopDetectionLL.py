'''
Given a circular linked list, implement an algorithm that return
s the node at the beginning of the loop.

'''

def findBeginning(llist):
    slow = llist.head
    fast = llist.head

    while fast is not None and fast,next is not None: #loopsize - k steps into llist
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    slow = llist.head
    while(slow != fast):
        slow = slow.next
        fast = fast.next

    return fast
