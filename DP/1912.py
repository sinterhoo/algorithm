import sys


n = int(input())

numbers = list(map(int,sys.stdin.readline().split()))

dp = [0 for _ in range(n)]

dp[0] = numbers[0]

for i in range(1,n):
    dp[i] = max(numbers[i], dp[i-1]+numbers[i])

print(max(dp))
