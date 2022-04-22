# range n+1 로 초기화하면 왜 인덱스 에러..?
# -> N이 1일 경우 dp[2] 를 초기화 못시켜서!

n = int(input())


dp = [0 for _ in range(n+2)]
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746

print(dp[n])