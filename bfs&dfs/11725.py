import sys
sys.setrecursionlimit(10**6)

n = int(input())

node = [[] for _ in range(n+1)]
check = [0]*(n+1)

for i in range(n-1):
    x,y = map(int, sys.stdin.readline().split())
    node[x].append(y)
    node[y].append(x)

check[1] = 1
def dfs(node, v, check):
    
    for i in node[v]:
        if check[i] == 0:
            check[i] = v
            dfs(node, i, check)

dfs(node, 1, check)

for i in range(2, n+1):
    print(check[i])

