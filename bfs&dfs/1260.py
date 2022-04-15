import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())

list1 = []

for i in range(m):
    x1,x2 = map(int, sys.stdin.readline().split())
    list1.append([max(x1, x2), min(x1, x2)])
    list1.append([min(x1,x2), max(x1,x2)])
list1.sort()
visited = [False] * (n+1)


def dfs(list1, n, visited):
    visited[n] = True
    print(n, end=' ')

    for i in range(len(list1)):
        for j in range(2):
            if not visited[list1[i][j]] and n in list1[i]:
                dfs(list1, list1[i][j], visited)

def bfs(list1, n, visited):
    visited[n] = True
    list2 = deque([])
    list2.append(n)
    while list2:
        n = list2.popleft()
        print(n, end=' ')
        for i in range(len(list1)):
            for j in range(2):
                if not visited[list1[i][j]] and n in list1[i]:
                    list2.append(list1[i][j])
                    visited[list1[i][j]] = True


dfs(list1, v, visited)
print()
visited = [False] * (n+1)
bfs(list1, v, visited)
