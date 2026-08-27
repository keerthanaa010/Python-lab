class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:

    
    def height(self, node):
        if node is None:
            return 0
        return node.height

    
    def get_balance(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    
    def right_rotate(self, y):
        x = y.left
        t2 = x.right

        x.right = y
        y.left = t2

        y.height = 1 + max(self.height(y.left),
                           self.height(y.right))
        x.height = 1 + max(self.height(x.left),
                           self.height(x.right))

        return x

    
    def left_rotate(self, x):
        y = x.right
        t2 = y.left

        y.left = x
        x.right = t2

        x.height = 1 + max(self.height(x.left),
                           self.height(x.right))
        y.height = 1 + max(self.height(y.left),
                           self.height(y.right))

        return y

    
    def insert(self, node, key):

        if node is None:
            return Node(key)

        if key < node.key:
            node.left = self.insert(node.left, key)
        elif key > node.key:
            node.right = self.insert(node.right, key)
        else:
            print("Enrollment ID already exists!")
            return node

        
        node.height = 1 + max(self.height(node.left),
                              self.height(node.right))

        balance = self.get_balance(node)

        
        if balance > 1 and key < node.left.key:
            return self.right_rotate(node)

        
        if balance < -1 and key > node.right.key:
            return self.left_rotate(node)

        
        if balance > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        
        if balance < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    
    def min_value_node(self, node):
        current = node

        while current.left is not None:
            current = current.left

        return current

    
    def delete(self, node, key):

        if node is None:
            return node

        if key < node.key:
            node.left = self.delete(node.left, key)

        elif key > node.key:
            node.right = self.delete(node.right, key)

        else:
            
            if node.left is None:
                return node.right

            elif node.right is None:
                return node.left

            
            temp = self.min_value_node(node.right)
            node.key = temp.key
            node.right = self.delete(node.right, temp.key)

        if node is None:
            return node

        
        node.height = 1 + max(self.height(node.left),
                              self.height(node.right))

        balance = self.get_balance(node)

        
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.right_rotate(node)

        
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

    
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.left_rotate(node)

        
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    
    def search(self, node, key):

        if node is None:
            return False

        if key == node.key:
            return True

        if key < node.key:
            return self.search(node.left, key)

        return self.search(node.right, key)

    
    def inorder(self, node):

        if node is not None:
            self.inorder(node.left)
            print(node.key, end=" ")
            self.inorder(node.right)

    
    def count(self, node):

        if node is None:
            return 0

        return 1 + self.count(node.left) + self.count(node.right)



tree = AVLTree()
root = None

while True:
    print("\n--- AVL TREE MENU ---")
    print("1. Insert Enrollment")
    print("2. Delete Enrollment")
    print("3. Search Enrollment")
    print("4. Display Enrollments")
    print("5. Count Total Enrollments")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        enrollment_id = int(input("Enter Enrollment ID: "))
        root = tree.insert(root, enrollment_id)
        print("Enrollment inserted successfully.")

    elif choice == 2:
        enrollment_id = int(input("Enter Enrollment ID to delete: "))

        if tree.search(root, enrollment_id):
            root = tree.delete(root, enrollment_id)
            print("Enrollment deleted successfully.")
        else:
            print("Enrollment ID not found.")

    elif choice == 3:
        enrollment_id = int(input("Enter Enrollment ID to search: "))

        if tree.search(root, enrollment_id):
            print("Enrollment ID found.")
        else:
            print("Enrollment ID not found.")

    elif choice == 4:
        print("Enrollment IDs in sorted order:")
        tree.inorder(root)
        print()

    elif choice == 5:
        print("Total Enrollments:", tree.count(root))

    elif choice == 6:
        print("Program ended.")
        break

    else:
        print("Invalid choice!")
