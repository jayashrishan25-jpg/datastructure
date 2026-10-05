# BFS and DFS

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def bfs(start):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)

        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])

    return visited

def dfs(node, visited=None):
    if visited is None:
        visited = []

    visited.append(node)

    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(neighbour, visited)

    return visited

print("BFS:", bfs('A'))
print("DFS:", dfs('A'))