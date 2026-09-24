from collections import deque
graph = {
    1: [2, 3],
    2: [1, 3, 5],
    3: [1, 2, 4],
    4: [3, 5],
    5: [2, 4, 6],
    6: [5, 7],
    7: [6]
}
def bfs(start):
    visited = set()
    queue = deque([start])
    result = []
    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.add(node)
            result.append(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)

    return result
def dfs(start):
    visited = set()
    result = []

    def visit(node):
        visited.add(node)
        result.append(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                visit(neighbour)

    visit(start)
    return result
start = 1
print("BFS Traversal:", bfs(start))
print("DFS Traversal:", dfs(start))
