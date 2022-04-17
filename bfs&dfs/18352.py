import sys
from collections import deque

def bfs (node, n, visited, k):
    visited[n] = 1
    move = deque([])
    for i in node[n]:
        move.append(i)
        visited[i] = visited[n] + 1

    while move:
        city = move.popleft()
        for i in node[city]:
            if visited[i] == 0:
                move.append(i)
                visited[i] = visited[city] + 1
    check = 0
    for i in range(1, len(visited)):
        if i != n and visited[i]-1 == k:
            print(i)
            check = check + 1
    if check == 0:
        print(-1)

n,m,k,z = map(int, input().split())


node = [[] for _ in range(n+1)]

visited= [0 for _ in range(n+1)]

for i in range(m):
    x,y = map(int, sys.stdin.readline().split())
    node[x].append(y)

bfs(node, z, visited, k)
