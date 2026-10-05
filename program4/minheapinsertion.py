import heapq

heap = []

heapq.heappush(heap, 30)
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)
heapq.heappush(heap, 5)
heapq.heappush(heap, 15)

print("Min Heap:", heap)

print("Minimum element:", heap[0])