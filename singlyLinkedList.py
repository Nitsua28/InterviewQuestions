"""
Implement a singly linked list.
"""

class LinkedList:
	def __init__(self,head):
  		self.head = None

  def push_front(self,node):
  	if self.head != None:
    	nextNode = self.head #previous head is now next
      self.head = node #new head is node
      node.next = nextNode
    else:
    	self.head = node
  '''
  ---push_front test-----------------------------

  	-Regular test-

  	(23) -> (34) -> (56)
    push_front(14)

    nextNode(23)
    self.head(14)
    node.next(23)

    (14) -> (23) -> (34) -> (56)

    -Extreme case-

    ()
    push_front(14)

    self.head == None
    self.head(14)
--------------------------------------------------
'''
	def push_back(self,node):
  	if self.head == None:
    	self.head = node
    	return

  	temp = self.head

    while temp.next is not None:
      temp = temp.next

    temp.next = node
'''
  ---push_back test----------------------------------

  -regular-

  (23) -> (45)
  push_back(77)

  temp = 23

  temp = 45

  temp.next = 77

  (23) -> (45) -> (77)

  -extreme-

  ()
  push_back(8)

  self.head == None
  self.head = node

  (8)
  ---------------------------------------------------
  '''
  def insert(self,node, location):
    prev = 0

    if self.head is None:
    	self.head = node
    	return
  	if location == 1:
      node.next = temp
      self.head = node

    temp = self.head

    for i in range(1,location):
    	if temp is None:
      	return -1
      prev = temp
      temp = temp.next

    if prev.next is not None:
      prev.next = node
      node.next = temp
      return

    prev.next = node
  '''
  ---insert Test--------------------------------------

  -if head-

  (12) -> (35)
  insert(11, 1)

  prev = 0
  temp = 12

  location == 1
  node.next = 12
  self.head = 11

  (11) -> (12) -> (35)

  - if middle-

  (12) -> (35) -> (66)
  insert(11, 3)

  prev = 0
  temp = 12

  i = 1
  prev = 12
  temp = 35

  i = 2
  prev = 35
  temp = 66


  prev.next = 11
  node.next = 66

  -if end-

  (12) -> (35)
  insert(11,3)

  prev = 0
  temp = 12

  i = 1
  prev = 12
  temp = 35

  i = 2
  prev = 35
  temp = None



  temp.next = 11

  (12) -> (35) -> (11)

  -extreme-
  ()

	insert(11,6)

	prev = 0

	self.head == None

	return None

	(11)

	(1)
  insert(11,2)

  prev = 0
  temp = 1

  i = 1
  prev = 1
  temp = None

  prev.next = 11

  -if location too great-

  (34) -> (56) -> (87)
  insert(11,6)

  prev = 0
  temp = 34

  i = 1
  prev = 34
  temp = 56

  i = 2
  prev = 56
  temp = 87

  i = 3
  prev = 87
  temp = None

  temp == None

  return error
  ------------------------------------------------------
  '''
  def pop_front(self):
  	if self.head != None:
      temp = self.head
      self.head = temp.next
      temp = None
  '''
  ---pop_front test--------------------------------------

  	-Regular Test-

    (23) -> (12)
    pop_front()

    temp = (23)
    self.head = (12)
    temp = None

    (12)

    -extreme test-

    ()
    pop_front()

    self.head == None

    ()
  ---------------------------------------------------------
  '''
  def pop_back(self):
  	if self.head == None:
    	return
  	temp = self.head
    prev = None

    while temp.next is not None:
      prev = temp
      temp = temp.next

    prev.next = None
    temp = none
  '''
  ---pop_back test-----------------------------------------

    -regular test-

    (12) -> (36)
    pop_back()

    temp = (12)
    prev = None

    prev= (12)
    temp = (36)

    prev.next = None

    -extreme cases-

    ()
    pop_back()

    self.head == None
    return nothing


  -------------------------------------------------------------
  '''
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

  '''
  ---remove Test--------------------------------------------------

  -if head-

  (12) -> (33)
  remove(12)

  temp = 12
  prev = None

	temp.data == key

  prev.next = 33
  temp = 33

  (33)

  -if middle-

  (23) -> (56) -> (78)
  remove(56)

  temp = 23
  prev = None

  prev = 23
  temp = 56

  temp.data == key

  prev.next = 78
  temp = 78

  (23) -> (78)

  -if end-

  (23) -> (56)
  remove(56)

  temp = 23
  prev = None

  prev = 23
  temp = 56

  temp.data is key

  prev.next = None
  temp = None

  (23)

  -extreme-

  ()
  remove(999)

  self.head == None
  return None
  ()

  -if multiple keys-

  (23) -> (24) -> (24) -> (56)
  remove(24)

  temp = 23
  prev = None

  prev = 23
  temp = 24

  temp.data == key

  prev.next = 24
  temp = 24

	prev.next = 56
  temp = 56

  (23) -> (56)


---------------------------------------------------------
'''

class Node:
  def __init__(self,data,next):
  	self.data = data
    self.next = next
