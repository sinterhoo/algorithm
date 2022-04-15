import sys
import heapq


n = int(input())

min_heap = []

sum_temp = 0

for i in range(n):
    temp = int(sys.stdin.readline())
    heapq.heappush(min_heap, temp)

if len(min_heap) == 1:
    print(0)
else:
    while min_heap:
        result = heapq.heappop(min_heap)
        result2 = heapq.heappop(min_heap)
        sum_temp = sum_temp + result+result2
        heapq.heappush(min_heap,result+result2)

        if len(min_heap) == 1:
            break

    print(sum_temp)