import heapq

heap = []

for value in [40, 20, 10, 30, 50]:
    heapq.heappush(heap, value)

print("Heap:", heap)

deleted = heapq.heappop(heap)

print("Deleted element:", deleted)
print("Heap after deletion:", heap)