'''
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
