import sys
import bisect


n, k = map(int, input().split())

level_list = [int(sys.stdin.readline()) for _ in range(n)]

level_list.sort()

left = 0
right = level_list[len(level_list)-1] + k
max_num = 0

while left <= right:
    mid = (left + right)//2
    temp = k

    index = bisect.bisect_left(level_list, mid)

    if (sum(level_list[:index+1])+k)//(index+1) > max_num:
        for i in level_list[:index+1]:
            gap = mid - i
            temp = temp - gap
            if temp < 0:
                right = mid-1
                break
        else:
            max_num = mid
            left = mid +1
    else:
        right = mid -1

print(max_num)