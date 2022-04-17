import sys
from telnetlib import BRK
sys.setrecursionlimit(10**6)

def dfs(ice, x,y, visited):
    visited[x][y] = True

    for i in pos:
        if x+i[0] > -1 and x+i[0] < len(ice) and y+i[1] > -1 and y+i[1] < len(ice[0]):
            if visited[x+i[0]][y+i[1]] == False and ice[x+i[0]][y+i[1]] != 0:
                dfs(ice, x+i[0], y+i[1], visited)
            elif ice[x+i[0]][y+i[1]] == 0 and visited[x+i[0]][y+i[1]] == False:
                if ice[x][y] > 0:
                    ice[x][y] = ice[x][y] -1

n,m = map(int, input().split())

ice = []
pos = [[1,0],[-1,0],[0,1],[0,-1]]

visited = [[False]*m for _ in range(n)]


for i in range(n):
    list1 = list(map(int, sys.stdin.readline().split()))
    ice.append(list1)
count = 0
while True:
    visited = [[False]*m for _ in range(n)]
    check = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] == False and ice[i][j] != 0:
                dfs(ice, i, j, visited)
                check = check + 1
    visited = [[False]*m for _ in range(n)]
    if check > 1:
        print(count)
        break
    if check == 0:
        print(0)
        break
    count +=1