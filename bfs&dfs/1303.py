import sys
sys.setrecursionlimit(10**5)
maps = []

m,n = map(int, input().split())
b_count = 0
w_count = 0
for _ in range(n):
    maps.append(list(sys.stdin.readline().rstrip()))

visited = [[False for _ in range(m)] for _ in range(n)]

def dfs(visited, now, maps, person):
    global count
    count +=1
    visited[now[0]][now[1]] = True
    pos = [[1,0],[-1,0],[0,1],[0,-1]]

    for i in pos:
        nx = now[0]+i[0]
        ny = now[1]+i[1]

        if 0<= nx < n and 0<= ny < m:
            if visited[nx][ny] == False and maps[nx][ny] == person:
                dfs(visited, [nx, ny], maps, person)


for i in range(n):
    for j in range(m):
        if visited[i][j] == False:
            count = 0
            dfs(visited, [i,j], maps, maps[i][j])
            if maps[i][j] == 'W':
                w_count += count**2
            else:
                b_count += count**2
print(w_count, b_count)