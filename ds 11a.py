n = int(input("Enter the total number of users: "))
matrix = [[0 for _ in range(n)] for _ in range(n)]
adj_list = [[] for _ in range(n)]
e = int(input("Enter the number of connections: "))
print("Enter the connections (user1 user2):")
for i in range(e):
    u, v = map(int, input().split())

    
    matrix[u][v] = 1
    matrix[v][u] = 1 

    
    adj_list[u].append(v)
    adj_list[v].append(u) 


print("\nAdjacency Matrix:")
print(" ", end="")

for i in range(n):
    print(i, end=" ")

print()

for i in range(n):
    print(i, end=" ")
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()
print("\nAdjacency List:")

for i in range(n):
    print(i, "->", adj_list[i])
u, v = map(int, input("\nEnter two users to check connection: ").split())

if matrix[u][v] == 1:
    print("Using Adjacency Matrix: Users are directly connected.")
else:
    print("Using Adjacency Matrix: Users are not directly connected.")
if v in adj_list[u]:
    print("Using Adjacency List: Users are directly connected.")
else:
    print("Using Adjacency List: Users are not directly connected.")
