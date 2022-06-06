from collections import deque
import copy
from enum import Flag

n = int(input())

for _ in range(n):
    start,end = input().split()

    move = deque()
    move.append([str(start),""])
    visited = [False] * 10000
    while move:
        now,answer = move.popleft()
        visited[int(now)] = True
        if int(now) == int(end):
            print(answer)
            break
        temp_now = now
        for i in range(4):
            now = temp_now
            temp_answer = answer
            if i == 0:
                if visited[int(now)*2%10000] == False:
                    temp_answer+='D'
                    move.append([str(int(now)*2%10000),temp_answer])
                    visited[int(now)*2%10000] = True
            elif i == 1:
                if now == '0':
                    now = 9999
                else:
                    now = int(now)-1
                if visited[now] == False:
                    temp_answer+='S'
                    visited[now] = True
                    move.append([str(now),temp_answer])
            elif i == 2:
                while len(now) != 4:
                    now = '0'+now
                now = deque(now)
                now.rotate(-1)
                now = ''.join(now)
                if visited[int(now)] == False:
                    temp_answer+='L'
                    visited[int(now)] = True
                    move.append([now,temp_answer])
            else:
                while len(now) != 4:
                    now = '0'+now
                now = deque(now)
                now.rotate(1)
                now = ''.join(now)
                if visited[int(now)] == False:
                    temp_answer+='R'
                    visited[int(now)] = True
                    move.append([now,temp_answer])

    


