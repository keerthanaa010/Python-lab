heap = []

def insert(job, priority):
    heap.append((priority, job))
    i = len(heap) - 1

    while i > 0:
        p = (i - 1) // 2
        if heap[i][0] > heap[p][0]:
            heap[i], heap[p] = heap[p], heap[i]
            i = p
        else:
            break

def delete_max():
    if not heap:
        print("Heap is empty")
        return

    max_job = heap[0]
    heap[0] = heap[-1]
    heap.pop()

    i = 0
    while True:
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i

        if left < len(heap) and heap[left][0] > heap[largest][0]:
            largest = left

        if right < len(heap) and heap[right][0] > heap[largest][0]:
            largest = right

        if largest != i:
            heap[i], heap[largest] = heap[largest], heap[i]
            i = largest
        else:
            break

    print("Deleted Job:", max_job[1])
    print("Priority:", max_job[0])

def peek():
    if heap:
        print("Highest Priority Job:", heap[0][1])
        print("Priority:", heap[0][0])
    else:
        print("Heap is empty")

def display():
    print("Jobs in Heap Order:")
    for priority, job in heap:
        print(job, "-", priority)


# Main Program
while True:
    print("\n1. Insert Job")
    print("2. Delete Highest Priority Job")
    print("3. Peek Highest Priority Job")
    print("4. Display All Jobs")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        job = input("Enter Job Name: ")
        priority = int(input("Enter Priority: "))
        insert(job, priority)

    elif ch == 2:
        delete_max()

    elif ch == 3:
        peek()

    elif ch == 4:
        display()

    elif ch == 5:
        break

    else:
        print("Invalid Choice")
