import sys

n = int(input())

nums =[list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [nums[0][0]]

for i in nums:
    dp.append(i[1])

print(dp)

maps = [[0 for _ in range(n)] for _ in range(n)]


for i in range(n):
    for j in range(n):
        if i >= j:
            continue
        if i > 0:
            sum = 1
            for k in range(i-1, j+1):
                sum *= dp[k]
            maps[i][j] = maps[i-1][j-1] + sum
        else:
            sum = 1
            for k in range(i-1, j+1):
                sum *= dp[k]
            maps[i][j] = maps[i][j-1] + sum

print(maps)