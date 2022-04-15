import sys

n,m = map(int, input().split())

house = [int(sys.stdin.readline()) for _  in range(n)]

house.sort()

left = 0
right = house[len(house)-1]
result = 0

while left <= right:
    mid = (left+right)//2
    share_count = m-1
    choose_house = house[0]
    for i in house:
        if i - choose_house >= mid:
            share_count = share_count - 1
            choose_house = i
        if share_count == 0:
            result = mid
            break
    if share_count > 0:
        right = mid -1
    else:
        left = mid +1

print(result)