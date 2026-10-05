# Graph using Adjacency List

graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 4, 5],
    4: [2, 3, 5],
    5: [3, 4]
}

def bfs(start):
    visited = set()
    queue = [start]

    print("BFS:", end=" ")

    while queue:
        node = queue.pop(0)

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)

def dfs(node, visited):
    visited.add(node)
    print(node, end=" ")

    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(neighbour, visited)

bfs(1)

print()
print("DFS:", end=" ")
dfs(1, set())