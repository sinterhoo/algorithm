import heapq
import sys

answer = []

n = int(input())

for i in range(n):
    order = int(sys.stdin.readline())

    if order == 0:
        if len(answer) == 0:
            print(0)
        else:
            temp = heapq.heappop(answer)
            print(temp[1])
    else:
        heapq.heappush(answer,(-order, order))

