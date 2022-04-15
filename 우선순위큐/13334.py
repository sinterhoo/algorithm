""" import sys
import heapq
from collections import deque

n = int(input())

house = []

list1 = deque([])

maxs = 0
temp_start = 0                  #가장 처음 선분의 시작점
temp_end = 0                    #가장 처음 선분의 끝점

for i in range(n):
    x1,x2 = map(int, sys.stdin.readline().split())
    length = abs(x1-x2)
    pos = max(x1,x2)
    heapq.heappush(house,(pos, length))

d = int(input())
road = sorted(house, key=lambda k : (k[0], -k[1]))      # 끝점(오름차순), 선분의 길이(내림차순)

for i in road:
    if i[1] <= d:
        if len(list1) == 0:                 # 선분이 하나도 안들어 있으면 그 선분 저장
            temp_start = i[0] - i[1]
            temp_end = i[0]
            list1.append(i)
        else:
            if temp_start + d < i[0]:       # 만약 첫 선분의 끝보다 새로운 선분의 끝이 멀리 있다면 검증
                while list1:
                    if list1[0][0] - list1[0][1] + d < i[0]:    # 모든 선분에 대해서 검증, 범위를 벗어났다면 pop
                        list1.popleft()
                    else:
                        break
            if i[0] - i[1] < temp_start:
                list1.appendleft(i)
                temp_end = list1[0][0]                  # 다시 첫 선분의 시작점, 끝점 저장
                temp_start = list1[0][0] - list1[0][1]
            else:
                list1.append(i)
                temp_end = list1[0][0]                  # 다시 첫 선분의 시작점, 끝점 저장
                temp_start = list1[0][0] - list1[0][1]       
    maxs = max(maxs, len(list1))

print(maxs) """


# 논리 자체는 맞았음, 근데 일반 큐로 구현을 하면 틀리고 최소힙으로 구현을 하면 가능
# 이미 정렬된 값이 들어가서 괜찮을거라 판단했는데 이유가 뭘까 알아보자
import sys
from heapq import heappop, heappush


n = int(input())

house = [sorted(list(map(int, sys.stdin.readline().split()))) for _ in range(n)]
d = int(input())

road = sorted(house, key= lambda x : (x[1], x[0]))
road = list(filter(lambda x : abs(x[0] - x[1]) <= d, road))

answer = []
max_count = 0

for i in road:
    if len(answer) == 0:
        heappush(answer, i)
    else:
        while answer:
            if answer[0][0] + d < i[1]:
                heappop(answer)
            else:
                break
        heappush(answer, i)
    max_count = max(max_count, len(answer))


print(max_count)