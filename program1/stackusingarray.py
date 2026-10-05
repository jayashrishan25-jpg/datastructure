stack = []

def push(x):
    stack.append(x)
    print(x, "pushed")

def pop():
    if stack:
        print(stack.pop(), "popped")
    else:
        print("Stack Underflow")

def peek():
    if stack:
        print("Top element:", stack[-1])
    else:
        print("Stack is empty")

push(10)
push(20)
push(30)
peek()
pop()
peek()

print("Stack:", stack)