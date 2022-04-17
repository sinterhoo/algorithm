import sys
from collections import deque


n,m = map(int, input().split())

students =[[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

counts = [0 for _ in range(n+1)]

for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    students[a].append(b)
    counts[b] = counts[b]+1

def solved(students, counts, visited):

    move = deque()
    for i in range(1, len(counts)):
        if counts[i] == 0:
            move.append(i)
            visited[i] = True

    while move:
        x = move.popleft()
        print(x, end= ' ')
        for i in students[x]:
            counts[i] = counts[i] - 1
            if visited[i] == False and counts[i] == 0:
                move.append(i)
                visited[i] = True    

solved(students, counts, visited)