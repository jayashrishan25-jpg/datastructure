size = 5
queue = [None] * size
front = -1
rear = -1

def insert(value):
    global front, rear

    if (rear + 1) % size == front:
        print("Circular Queue is Full")
        return

    if front == -1:
        front = 0

    rear = (rear + 1) % size
    queue[rear] = value
    print(value, "inserted")

def delete():
    global front, rear

    if front == -1:
        print("Queue is Empty")
        return

    print(queue[front], "deleted")

    if front == rear:
        front = rear = -1
    else:
        front = (front + 1) % size

insert(10)
insert(20)
insert(30)

delete()
insert(40)

print("Circular Queue:", queue)