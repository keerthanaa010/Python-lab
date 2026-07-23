SIZE = 5

queue = [0] * SIZE
front = -1
rear = -1


def enqueue(value):
    global front, rear

    if rear == SIZE - 1:
        print("Queue is FULL!!! Insertion is not possible!!!")
    else:
        rear += 1
        queue[rear] = value

        if front == -1:
            front = 0

        print("Element inserted successfully")


def dequeue():
    global front, rear

    if front == -1 or front > rear:
        print("Queue is EMPTY!!!")
    else:
        print("Deleted element:", queue[front])
        front += 1

        if front > rear:
            front = -1
            rear = -1


def isEmpty():
    if front == -1:
        return True
    else:
        return False


def size():
    if isEmpty():
        return 0
    else:
        return rear - front + 1


def show():
    if isEmpty():
        print("Queue is EMPTY!!!")
    else:
        print("Queue elements are:")
        for i in range(front, rear + 1):
            print(queue[i], end=" ")
        print()

while True:
    print("\n--- ARRAY IMPLEMENTATION OF QUEUE ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. IsEmpty")
    print("4. Size")
    print("5. Show")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter the value: "))
        enqueue(value)

    elif choice == 2:
        dequeue()

    elif choice == 3:
        if isEmpty():
            print("Queue is EMPTY")
        else:
            print("Queue is NOT EMPTY")

    elif choice == 4:
        print("Size of queue:", size())

    elif choice == 5:
        show()

    elif choice == 6:
        print("Program terminated")
        break

    else:
        print("Invalid choice")


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


front = None
rear = None


def enqueue(value):
    global front, rear

    newNode = Node(value)

    # If queue is empty
    if rear is None:
        front = newNode
        rear = newNode
    else:
        rear.next = newNode
        rear = newNode

    print("Element inserted successfully")


def dequeue():
    global front, rear

    # Check whether queue is empty
    if front is None:
        print("Queue is Empty")
    else:
        temp = front
        print("Deleted element:", temp.data)

    
        if front is None:
            rear = None


def display():
    if front is None:
        print("Queue is Empty!!!")
    else:
        temp = front

        print("Queue elements:")
        while temp is not None:
            print(temp.data, end=" --> ")
            temp = temp.next

        print("NULL")



while True:
    print("\n--- LINKED LIST IMPLEMENTATION OF QUEUE ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter the value: "))
        enqueue(value)

    elif choice == 2:
        dequeue()

    elif choice == 3:
        display()

    elif choice == 4:
        print("Program terminated")
        break

    else:
        print("Invalid choice")


​
