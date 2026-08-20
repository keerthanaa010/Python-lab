class Node:
    def __init__(self, name, time, purpose):
        self.name = name
        self.time = time
        self.purpose = purpose
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    
    def insert(self, name, time, purpose):
        new_node = Node(name, time, purpose)

        if self.root is None:
            self.root = new_node
            return

        current = self.root

        while True:
            if name < current.name:
                if current.left is None:
                    current.left = new_node
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    break
                current = current.right

    
    def search(self, name):
        current = self.root

        while current:
            if name == current.name:
                print("Visitor Found!")
                print("Name:", current.name)
                print("Entry Time:", current.time)
                print("Purpose:", current.purpose)
                return

            elif name < current.name:
                current = current.left
            else:
                current = current.right

        print("Visitor not found.")

    
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.name, "|", node.time, "|", node.purpose)
            self.inorder(node.right)

    
    def preorder(self, node):
        if node:
            print(node.name, "|", node.time, "|", node.purpose)
            self.preorder(node.left)
            self.preorder(node.right)

    
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.name, "|", node.time, "|", node.purpose)

    
    def count(self, node):
        if node is None:
            return 0
        return 1 + self.count(node.left) + self.count(node.right)



bst = BST()

while True:
    print("\n--- LOG BOOK MANAGEMENT ---")
    print("1. Insert Log Entry")
    print("2. Search Log Entry")
    print("3. Display Inorder")
    print("4. Display Preorder")
    print("5. Display Postorder")
    print("6. Count Total Entries")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter Visitor Name: ")
        time = input("Enter Entry Time: ")
        purpose = input("Enter Purpose: ")

        bst.insert(name, time, purpose)
        print("Log entry inserted successfully.")

    elif choice == 2:
        name = input("Enter Visitor Name to search: ")
        bst.search(name)

    elif choice == 3:
        print("\nVisitor Logs (Sorted Order):")
        bst.inorder(bst.root)

    elif choice == 4:
        print("\nVisitor Logs (Preorder):")
        bst.preorder(bst.root)

    elif choice == 5:
        print("\nVisitor Logs (Postorder):")
        bst.postorder(bst.root)

    elif choice == 6:
        print("Total Log Entries:", bst.count(bst.root))

    elif choice == 7:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
