class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def insert(self, data):
        new = Node(data)

        if self.rear is None:
            self.front = self.rear = new
        else:
            self.rear.next = new
            self.rear = new

        print(data, "inserted")

    def delete(self):
        if self.front is None:
            print("Queue is empty")
        else:
            print(self.front.data, "deleted")
            self.front = self.front.next

q = Queue()

q.insert(10)
q.insert(20)
q.insert(30)

q.delete()
q.delete()