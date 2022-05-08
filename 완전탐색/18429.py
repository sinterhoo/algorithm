import sys
from itertools import permutations

n,k = map(int, input().split())

nums = list(map(int, sys.stdin.readline().split()))

nums = list(permutations(nums, n))

count = 0
for i in nums:
    start = 500
    for j in i:
        start = start - k + j
        if start < 500:
            break
    else:
        count +=1

print(count)
