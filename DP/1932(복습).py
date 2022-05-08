import sys


n = int(input())

nums = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(len(nums[i])):
        if j == 0:
            nums[i][j] = nums[i][j] + nums[i-1][j]
            continue
        if j == len(nums[i])-1:
            nums[i][j] = nums[i][j] + nums[i-1][j-1]
            continue
        nums[i][j] = max(nums[i][j] + nums[i-1][j-1], nums[i][j] + nums[i-1][j])


print(max(nums[n-1]))