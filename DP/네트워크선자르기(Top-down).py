dp = [-1 for _ in range(50)]

def solved(n):
    if dp[n] != -1:
        return dp[n]
    if n == 1 or n == 2:
        return n
    dp[n] = solved(n-1) + solved(n-2)
    return dp[n]

n = int(input())

print(solved(n))


