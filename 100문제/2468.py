import sys
sys.setrecursionlimit(10**5)


def dfs(visited, land, now, N):
    pos = [[1,0], [0,1], [-1,0], [0,-1]]
    visited[now[0]][now[1]] = True

    for i in pos:
        n_step = [now[0]+i[0], now[1]+i[1]]
        if n_step[0] >= 0 and n_step[0] < N and n_step[1] >= 0 and n_step[1] < N:
            if visited[n_step[0]][n_step[1]] == False and land[n_step[0]][n_step[1]] > 0:
                dfs(visited, land, [n_step[0], n_step[1]], N)


N = int(input())

land = []
max_num = 0
for _ in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    land.append(temp)
    max_num = max(max(temp), max_num)


result = 0
for i in range(max_num):
    count = 0
    visited = [[False for _ in range(N)] for _ in range(N)]

    for k in range(N):
        for m in range(N):
            if visited[k][m] == False and land[k][m] > 0:
                dfs(visited, land, [k,m], N)
                count +=1
    else:
        result = max(result, count)
    
    for k in range(N):
        for m in range(N):
            if land[k][m] > 0 :
                land[k][m] -= 1


print(result)