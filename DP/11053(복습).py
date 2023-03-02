import sys


n = int(input())

nums = list(map(int, sys.stdin.readline().split()))

dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(0, i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))