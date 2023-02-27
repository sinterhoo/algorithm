def solution(triangle):
    answer = 0
    n = len(triangle)
    
    dp = [[0]*i for i in range(1,n+1)]
    dp[0][0] = triangle[0][0]
    if n > 1:
        dp[1][0] = triangle[0][0] + triangle[1][0]
        dp[1][1] = triangle[0][0] + triangle[1][1]
    for i in range(2,n):
        for j in range(len(dp[i])):
            if j != 0 and j != len(dp[i])-1:
                dp[i][j] = max(dp[i-1][j] + triangle[i][j], dp[i-1][j-1] + triangle[i][j])
            elif j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            else:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
    
    answer = max(dp[n-1])
    return answer


solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])