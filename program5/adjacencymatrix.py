# Graph using Adjacency Matrix

graph = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 1, 1],
    [0, 1, 1, 0, 1],
    [0, 0, 1, 1, 0]
]

def bfs(start):
    visited = [False] * 5
    queue = [start]
    visited[start] = True

    print("BFS:", end=" ")

    while queue:
        node = queue.pop(0)
        print(node + 1, end=" ")

        for i in range(5):
            if graph[node][i] == 1 and not visited[i]:
                visited[i] = True
                queue.append(i)

def dfs(node, visited):
    visited[node] = True
    print(node + 1, end=" ")

    for i in range(5):
        if graph[node][i] == 1 and not visited[i]:
            dfs(i, visited)

bfs(0)

print()
print("DFS:", end=" ")
visited = [False] * 5
dfs(0, visited)