import sys
from heapq import heappop, heappush

n = int(input())
m = int(input())

node = [[] for _ in range(n+1)]

for i in range(m):
    start, end, cost = map(int, sys.stdin.readline().split())
    node[start].append([cost, end])

start, end = map(int, input().split())

costs = [2000000000 for _ in range(n+1)]

move = []
heappush(move, [0, start])
costs[start] = 0

while move:
    cost, city = heappop(move)
    if costs[city] < cost:
        continue
    elif city != end:
        for i in node[city]:
            if costs[i[1]] > costs[city] + i[0]:
                heappush(move, i)
                costs[i[1]] = costs[city] + i[0]

print(costs[end])

