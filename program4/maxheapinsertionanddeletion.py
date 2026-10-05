import heapq

heap = []

values = [10, 40, 20, 50, 30]

for value in values:
    heapq.heappush(heap, -value)

print("Max Heap:", [-x for x in heap])

deleted = -heapq.heappop(heap)

print("Deleted maximum:", deleted)
print("Heap after deletion:", [-x for x in heap])