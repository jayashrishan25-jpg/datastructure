class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new = Node(data)
        new.next = self.top
        self.top = new
        print(data, "pushed")

    def pop(self):
        if self.top is None:
            print("Stack Underflow")
        else:
            print(self.top.data, "popped")
            self.top = self.top.next

    def peek(self):
        if self.top:
            print("Top:", self.top.data)
        else:
            print("Stack is empty")

s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.peek()
s.pop()
s.peek()