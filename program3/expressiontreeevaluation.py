class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def evaluate(root):
    if root.left is None and root.right is None:
        return int(root.value)

    left = evaluate(root.left)
    right = evaluate(root.right)

    if root.value == '+':
        return left + right
    elif root.value == '-':
        return left - right
    elif root.value == '*':
        return left * right
    elif root.value == '/':
        return left / right

# Expression: (10 + 5) * 2
root = Node('*')
root.left = Node('+')
root.right = Node('2')

root.left.left = Node('10')
root.left.right = Node('5')

print("Expression: (10 + 5) * 2")
print("Result:", evaluate(root))