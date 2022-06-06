import sys
from collections import deque

m,n = map(int, input().split())
n -=1
m -=1

miro = []
pos = [[1,0],[-1,0],[0,1],[0,-1]]
visited = [[False for _ in range(m+1)] for _ in range(n+1)]
for _ in range(n+1):
    miro.append(list(sys.stdin.readline().rstrip()))

move = deque()
count = 0
move.append([0,0,count])
visited[0][0] = True
check = 0
while move:
    now = move.popleft()
    visited[now[0]][now[1]] = True
    count = now[2]
    if now[0] == n and now[1] == m:
        if check == 0 or int(miro[n][m]) > count:
            miro[n][m] = str(count)
            check = 1
            continue
    for i in pos:
        n_x = now[0]+i[0]
        n_y = now[1]+i[1]
        if 0<= n_x <=n and 0<=n_y <=m:
            if visited[n_x][n_y] == False and miro[n_x][n_y] != '0':
                move.append([n_x,n_y,count+1])
            elif visited[n_x][n_y] == False and miro[n_x][n_y] == '0':
                move.append([n_x,n_y,count])
print(miro[n][m])