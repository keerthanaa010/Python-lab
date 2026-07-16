class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Playlist:
    def __init__(self):
        self.head = None

    def insert(self, song):
        new = Node(song)
        if not self.head:
            self.head = new
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new

    def delete(self, song):
        temp = self.head

        if temp and temp.data == song:
            self.head = temp.next
            return

        while temp and temp.next:
            if temp.next.data == song:
                temp.next = temp.next.next
                return
            temp = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")



p = Playlist()

while True:
    print("\n1. Insert  2. Delete  3. Display  4. Exit")
    ch = int(input("Choice: "))

    if ch == 1:
        p.insert(input("Enter song: "))

    elif ch == 2:
        p.delete(input("Delete song: "))

    elif ch == 3:
        p.display()

    elif ch == 4:
        break

    else:
        print("Invalid choice!")
