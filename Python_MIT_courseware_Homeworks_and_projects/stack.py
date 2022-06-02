class Stack(object):
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.insert(0, item)
    
    def pop(self):
        if (self.isEmpty() != True):
            print("popping...", self.stack[0])
            return self.stack.pop(0)
        else:
            print("Stack is Empty!")

    def isEmpty(self):
        return self.stack == []

stack = Stack()
stack.push(5)
stack.push(6)
stack.pop()
stack.push(7)
stack.pop()
stack.pop()
stack.pop()
