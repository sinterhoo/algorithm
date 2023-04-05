## 웅덩이 x,y 값 반대로 검증해서 틀렸었음

def solution(m, n, puddles):
    answer = 0
    dp = [[0 for _ in range(m)] for _ in range(n)]
    
    dp[0][0] = 1
    
    for y in range(n):
        for x in range(m):
            if (y == 0 and x == 0) or ([x+1,y+1] in puddles):
                continue
            if y-1 >= 0 and x-1 >= 0:
                dp[y][x] = dp[y-1][x] + dp[y][x-1]
            elif y-1 < 0:
                dp[y][x] = dp[y][x-1]
            else:
                dp[y][x] = dp[y-1][x]       
    answer = dp[n-1][m-1] % 1000000007
    return answer