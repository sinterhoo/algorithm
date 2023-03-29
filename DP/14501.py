N = int(input())

dp = [0]*(N+1)

nums = []

for i in range(N):
    days,value = map(int, input().split())
    nums.append([days,value])

for k in range(N):
    now_value = max(dp[:k+1])
    now_value += nums[k][1]
    count = nums[k][0]

    if k+count <= N:
        dp[k+count] = max(dp[k+count], now_value)

print(max(dp))