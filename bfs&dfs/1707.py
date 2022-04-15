import sys
sys.setrecursionlimit(10**6)



def dfs(node, v, visited, color):
    global line
    if color == 2:
        color = 3
    elif color == 3:
        color = 2
    visited[v] = color

    for i in node[v]:
        if visited[i] == 0:
            dfs(node, i, visited, color)
        elif visited[v] == visited[i]:
            line = 1

k = int(input())

global line

for i in range(k):
    v,e = map(int, input().split())

    node = [[] for _ in range(v+1)]
    line = 0
    visited = [0]*(v+1)
    visited[0] = 1

    for i in range(e):
        x1, x2 = map(int, sys.stdin.readline().split())
        node[x1].append(x2)
        node[x2].append(x1)

    dfs(node, 1, visited, 3)
    while 0 in visited:                                     # 그래프가 꼭 전부 이어져있다는 보장은 없고 끊어진 두개 이상의 그래프가 들어올 경우
        dfs(node, visited.index(0), visited, 3)             # 그것을 체크하기 위해 모두 돌아준다.

    if line == 0:
        print("YES")
    else:
        print("NO")