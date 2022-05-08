import sys
from collections import deque

n,k = map(int, input().split())

left_list = list(sys.stdin.readline().rstrip())
right_list = list(sys.stdin.readline().rstrip())
check = 0
def solved(index, k, n ,pos, time):
    visited = [False for _ in range(n+1)]

    visited[index] = True

    move = deque()
    move.append([pos, n])
    check =0
    while move:
        for _ in range(len(move)):
            x = move.popleft()
            if x[1] > n-1:
                check = 1
                break
            if x[1] - 1 >time and visited[x[1]-1] == False:
                move.append([x[0],x[1]-1])
            if x[1]+1 > n or (visited[x[1]+1] == False and 
solved(0, k, n, 'left', 0)

if check ==0:
    print(check)