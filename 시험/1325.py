import sys
from collections import deque


n,m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    x,y = map(int, sys.stdin.readline().split())
    graph[y].append(x)

answer = [0]

max_count = -1
for i in range(1,n+1):
    move = deque()
    move.append(i)
    count = 0
    visited = [False]*(n+1)
    visited[i] = True
    while move:
        now = move.popleft()
        count +=1
        for k in graph[now]:
            if visited[k] == False:
                move.append(k)
                visited[k] = True
    if max_count == count:
        answer.append(i)
    elif max_count < count:
        answer = [i]
        max_count = count

for i in answer:
    print(i,end=' ')