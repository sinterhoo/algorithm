import sys
from heapq import heappop, heappush

r,s = map(int, input().split())

maps = []

start = []
end = []

for i in range(r):
    temp = list(sys.stdin.readline().rstrip())
    
    for k in range(len(temp)):
        if temp[k] == 'X':
            heappush(start, (-i, k))
        if temp[k] == '#':
            heappush(end, (i,k))
    maps.append(temp)

mins = 1e9
for j in end:
    for i in start:
        if i[1] == j[1]:
            mins = min(mins, abs(-i[0] - j[0]))
    if mins != 1e9:
        break
mins = mins-1
for i in start:
    maps[-i[0]+mins][i[1]] = 'X'
    maps[-i[0]][i[1]] = '.'

for i in range(r):
    sys.stdout.write(''.join(maps[i]))
    sys.stdout.write('\n')
