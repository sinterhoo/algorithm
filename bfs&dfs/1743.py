import sys
sys.setrecursionlimit(10**5)

def dfs(visited, now, maps):
    global count
    count +=1
    visited[now[0]][now[1]] = True

    pos = [[1,0],[-1,0],[0,1],[0,-1]]

    for i in pos:
        nx = now[0] + i[0]
        ny = now[1] + i[1]

        if 0<= nx < n and 0<= ny < m:
            if visited[nx][ny] == False and maps[nx][ny] == 1:
                dfs(visited,[nx,ny],maps) 

n,m,k = map(int, input().split())

maps = [[0 for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
for _ in range(k):
    x,y = map(int, sys.stdin.readline().split())
    maps[x-1][y-1] = 1

answer = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == False and maps[i][j] == 1:
            count = 0
            dfs(visited, [i,j], maps)
            answer = max(answer, count)

print(answer)
