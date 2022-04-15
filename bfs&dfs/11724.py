import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

node = [[] for _ in range(n+1)]
visited = [False] * (n+1)
visited[0] = True

for i in range(m):
    x1, x2 = map(int, sys.stdin.readline().split())
    node[x1].append(x2)
    node[x2].append(x1)

def dfs(node, v, visited):
    visited[v] = True

    for i in node[v]:
        if not visited[i]:
            dfs(node, i, visited)

count = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(node, i, visited)
        count = count+1

print(count)