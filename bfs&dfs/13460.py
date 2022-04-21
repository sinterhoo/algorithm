# 첫 접근 방식 -> 빨간공 먼저 굴리고, 파란공 굴리고 하는 방법으로 접근했습니다.
# 동시에 굴려지는걸 구현을 잘 못하겠어서 따로 구현했더니 예외사항이 발생했음 (같은 코스트로 R,B가 O에 들어갈때)
# 오래 고민하다가 결국 답 참고했습니다. 고슴도치랑 좀 비슷했던거 같기도 하고 연습이 필요하네요

import sys
from collections import deque
import copy


def bfs(maps, red, blue):
    pos = [(1,0),(-1,0),(0,1),(0,-1)]
    
    move = deque()
    move.append((red, blue))
    visited = []
    visited.append((red,blue))
    count = 0
    while move:
        for _ in range(len(move)):
            red, blue = move.popleft()
            if count > 10:
                print(-1)
                return
            if maps[red[0]][red[1]] == 'O':
                print(count)
                return
            for i in pos:
                nred = copy.copy(red)
                while True:
                    nred[0] += i[0]
                    nred[1] += i[1]
                    if maps[nred[0]][nred[1]] == '#':
                        nred[0] -= i[0]
                        nred[1] -= i[1]
                        break
                    if maps[nred[0]][nred[1]] == 'O':
                        break
                nblue = copy.copy(blue)
                while True:
                    nblue[0] += i[0]
                    nblue[1] += i[1]
                    if maps[nblue[0]][nblue[1]] == '#':
                        nblue[0] -= i[0]
                        nblue[1] -= i[1]
                        break
                    if maps[nblue[0]][nblue[1]] == 'O':
                        break
                if maps[nblue[0]][nblue[1]] == 'O':
                    continue
                if nred == nblue:
                    if abs(nred[0] - red[0]) + abs(nred[1] - red[1]) > abs(nblue[0] - blue[0]) + abs(nblue[1] - blue[1]):
                        nred[0] -= i[0]
                        nred[1] -= i[1]
                    else:
                        nblue[0] -= i[0]
                        nblue[1] -= i[1]
                if (nred,nblue) not in visited:
                    visited.append((nred,nblue))
                    move.append((nred,nblue))
        count +=1
    print(-1)


n,m = map(int, input().split())

maps = []

red = []
blue = []
goal = []

for i in range(n):
    temp = sys.stdin.readline().rstrip()
    maps.append(temp)
    if 'R' in temp:
        red = [i,temp.index('R')]
    if 'B' in temp:
        blue = [i,temp.index('B')]


bfs(maps, red, blue)

