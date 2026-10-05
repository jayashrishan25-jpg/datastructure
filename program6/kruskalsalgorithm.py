# Kruskal's Algorithm

edges = [
    (1, 2, 2),
    (1, 3, 3),
    (2, 3, 1),
    (2, 4, 4),
    (3, 4, 5)
]

edges.sort(key=lambda x: x[2])

parent = [0, 1, 2, 3, 4]

def find(x):
    while parent[x] != x:
        x = parent[x]
    return x

print("Edges in Minimum Spanning Tree:")

count = 0

for u, v, weight in edges:
    root_u = find(u)
    root_v = find(v)

    if root_u != root_v:
        print(u, "-", v, ":", weight)
        parent[root_v] = root_u
        count += 1

    if count == 3:
        break