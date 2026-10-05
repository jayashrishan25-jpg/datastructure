# Prim's Algorithm using Dictionary

graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 4},
    'C': {'A': 3, 'B': 1, 'D': 5},
    'D': {'B': 4, 'C': 5}
}

visited = {'A'}
mst = []

while len(visited) < len(graph):
    minimum = None

    for node in visited:
        for neighbour, weight in graph[node].items():
            if neighbour not in visited:
                if minimum is None or weight < minimum[2]:
                    minimum = (node, neighbour, weight)

    u, v, weight = minimum
    mst.append((u, v, weight))
    visited.add(v)

print("Minimum Spanning Tree:")

for u, v, weight in mst:
    print(u, "-", v, ":", weight)