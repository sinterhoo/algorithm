import sys


n = int(input())


score = [int(sys.stdin.readline()) for _ in range(n)]

dp = [0 for _ in range(n+1)]

dp[0] = 0
dp[1] = score[0]
if n >=2:
    dp[2] = score[1] + dp[1]
    if n>=3:
        dp[3] = max(score[0] + score[2], score[1] + score[2] )

        for i in range(3, n+1):
            dp[i] = max(dp[i-3] + score[i-2] +score[i-1], dp[i-2] + score[i-1])

print(dp[n])
