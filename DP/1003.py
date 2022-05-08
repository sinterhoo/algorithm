
n = int(input())
dp = [0 for _ in range(41)]


dp[0] = [1,0]
dp[1] = [0,1]


for i in range(2, 41):
    dp[i] = [dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1]]

for _ in range(n):
    temp = int(input())
    print(dp[temp][0],dp[temp][1])


