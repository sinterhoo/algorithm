from collections import deque

n = int(input())

n = n % 1000000007

dp = deque([1,1])


for _ in range(n-2):
    dp.append((dp[0] + dp[1])%1000000007)
    dp.popleft()

print(dp[-1])