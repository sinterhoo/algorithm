import sys


n = int(input())

nums = list(map(int, sys.stdin.readline().split()))

dp = [1 for _ in range(n)]

for i in range(n):
    last = 0
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i]  = max(dp[i], dp[j]+1)
print(dp)