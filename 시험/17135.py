import sys
sys.setrecursionlimit(10**5)


m,n,k = map(int, input().split())

visited = [[0 for _ in range(n)] for _ in range(m)]
count = 0
maxs = m*n
for _ in range(k):
    x1,y1,x2,y2 = map(int, sys.stdin.readline().split())
    
    for i in range(x1, x2):
        for j in range(y1, y2):
            if visited[j][i] == 0:
                visited[j][i] = 1
                count+=1


def dfs(visited, x):
    global cnt
    cnt +=1
    pos = [[1,0],[-1,0],[0,1],[0,-1]]
    visited[x[0]][x[1]] = 1

    for i in pos:
        n_dx = x[0] + i[0]
        n_dy = x[1] + i[1]
        if 0<= n_dx < m and 0<= n_dy < n:
            if visited[n_dx][n_dy] == 0:
                dfs(visited, [n_dx, n_dy])

vis = 0
nums = []
for i in range(n):
    for j in range(m):
        if visited[j][i] == 0:
            cnt = 0
            dfs(visited, [j,i])
            vis +=1
            nums.append(cnt)

print(vis)
nums.sort()
for i in nums:
    print(i, end=' ')