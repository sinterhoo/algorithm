import sys
from heapq import heappop, heappush


def bfs(miro, x,y, costs, n):
    pos = [[1,0],[-1,0],[0,1],[0,-1]]
    move = []
    visited = [[False for _ in range(n)] for _ in range(n)]
    heappush(move, [x,y])
    costs[x][y] = 0
    visited[x][y] = True

    while move:
        x,y = heappop(move)
        if x == n-1 and y == n-1:
            break
        for i in pos:
            next_step = [x+i[0], y+i[1]]
            if 0<= next_step[0] < n and 0<= next_step[1] < n :
                if miro[next_step[0]][next_step[1]] == '1':
                    if costs[next_step[0]][next_step[1]] > costs[x][y]:
                        costs[next_step[0]][next_step[1]] = costs[x][y]
                        heappush(move, next_step)
                    else:
                        continue
                elif costs[next_step[0]][next_step[1]] < costs[x][y] +1:
                    continue
                else:
                    costs[next_step[0]][next_step[1]] = costs[x][y] + 1
                    heappush(move, next_step)
    print(costs[n-1][n-1])





n = int(input())
miro = []

for _ in range(n):
    temp = list(sys.stdin.readline().rstrip())
    miro.append(temp)

costs = [[1e9 for _ in range(n)] for _ in range(n)]

bfs(miro, 0, 0, costs, n)