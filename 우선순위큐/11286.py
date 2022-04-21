from heapq import heappop, heappush
import sys

nums = []

n = int(input())

for i in range(n):
    temp = int(sys.stdin.readline())

    if temp != 0:
        heappush(nums, (abs(temp), temp))
    else:
        if len(nums) == 0:
            print(0)
        else:
            x = heappop(nums)
            print(x[1])
