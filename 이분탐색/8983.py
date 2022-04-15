import sys

m, n, l = map(int, input().split())

gun_list = list(map(int, sys.stdin.readline().split()))

animal_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

gun_list.sort()
animal_list.sort()

count = 0

for i in animal_list:
    left = i[0]+i[1] - l
    right = i[0]-i[1] + l

    start = 0
    end = len(gun_list)-1

    while start <= end:
        mid = (start + end)//2

        if gun_list[mid] < left:
            start = mid +1
        elif gun_list[mid] > right:
            end = mid-1
        else:
            count = count+1
            break

print(count)