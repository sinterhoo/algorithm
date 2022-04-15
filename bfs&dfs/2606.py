import sys
sys.setrecursionlimit(10**6)

n =int(input())                 # 컴퓨터 수
m = int(input())                # 간선 수

node = [[] for i in range(n+1)]
visited = [False] * (n+1)
for i in range(m):
    x,y = map(int, sys.stdin.readline().split())
    node[x].append(y)
    node[y].append(x)

def dfs(node, n, visited):
    visited[n] = True

    for i in node[n]:
        if not visited[i]:
            dfs(node, i, visited)


dfs(node, 1, visited)

print(visited.count(True)-1)

