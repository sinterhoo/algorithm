# 코드가 상당히 더러움
# 처음에 실패했던 이유 -> 물이 퍼지는걸 이상하게 구현했음
# 두번째 실패했던 이유 -> 무브 pop을 한번만 해줬음
# 두개의 문제점 모두 while문 안에 for문을 한번 더 돌림으로써 해결했음
# 함수 분화시키는게 더 깔끔했을지도?

import sys
from collections import deque


def bfs(maps,start,end,visited,water, water_visited):
    pos = [[1,0],[-1,0],[0,1],[0,-1]]
    move = deque()
    waters = deque()
    move.append(start)
    visited[start[0]][start[1]] = 0
    for i in water:
        waters.append([i[0],i[1]])
        water_visited[i[0]][i[1]] = True
    while move:
        waters_temp = deque()
        move_temp = deque()
        for k in range(len(waters)):
            x2,y2 = waters.popleft()
            for i in pos:
                next_step = [x2+i[0], y2+i[1]]
                if 0<=next_step[0]<len(maps) and 0<= next_step[1] < len(maps[0]):
                    if maps[next_step[0]][next_step[1]] == '.' and water_visited[next_step[0]][next_step[1]] == False:
                        waters_temp.append(next_step)
                        water_visited[next_step[0]][next_step[1]] = True
                        maps[next_step[0]][next_step[1]] = '*'
        waters = waters_temp
        for k in range(len(move)):
            x,y = move.popleft()

            for i in pos:
                next_step = [x+i[0], y+i[1]]
                if 0<=next_step[0]<len(maps) and 0<= next_step[1] < len(maps[0]):
                    if (maps[next_step[0]][next_step[1]] == '.' or maps[next_step[0]][next_step[1]] == 'D') and visited[next_step[0]][next_step[1]] == -1:
                        move_temp.append(next_step)
                        visited[next_step[0]][next_step[1]] = visited[x][y] + 1
        move = move_temp
    if visited[end[0]][end[1]] == -1:
        print("KAKTUS")
    else:
        print(visited[end[0]][end[1]])

r,c = map(int, input().split())

maps = []
start = []
end = []
water= []
for i in range(r):
    x = sys.stdin.readline().rstrip()
    if 'S' in x:
        start.append([i,x.index('S')])
    if 'D' in x:
        end.append([i,x.index('D')])
    if '*' in x:
        water.append([i,x.index('*')])
    maps.append(list(x))

visited = [[-1 for _ in range(c)] for _ in range(r)]
water_visited = [[False for _ in range(c)] for _ in range(r)]

bfs(maps, start[0], end[0],visited, water, water_visited)