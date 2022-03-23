class Stack():
    def __init__(self,l):
        self.list = l

    def pop (self):
        self.list.pop()

    def push (self,n):
        self.list.append(n)

    def peek(self):
        return self.list[-1]

    def size(self):
        return len(self.list)

    def isEmpty(self):
        if self.list:
            return False
        return True

blah = [1,2,3,4]

stack = Stack(blah)

print("Testing pop")

stack.pop()
print(stack.list)

print("Testing push")

stack.push(4)
print(stack.list)

print("Testing peek")
print(stack.peek())

print("Testing size")
print(stack.size())

print("Testing isEmpty")
print(stack.isEmpty())
