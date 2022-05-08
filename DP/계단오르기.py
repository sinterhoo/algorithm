
""" 바텀 업
n = int(input())


dp = [0 for _ in range(50)]

dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n]) """

# 탑 다운

n = int(input())
dp = [-1 for _ in range(50)]
def solve(n):
    if dp[n] != -1:
        return dp[n]
    if n == 1 or n== 2:
        return n
    
    dp[n] = solve(n-1) + solve(n-2)
    return dp[n]

solve(n)
print(dp[n])
