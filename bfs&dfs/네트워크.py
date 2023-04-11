def solution(n, computers):
    visited = [False for _ in range(n)]
    answer = 0
    
    def dfs(computers, now):
        for k in range(n):
            if visited[k] == False and computers[now][k] == 1:
                visited[k] = True
                dfs(computers, k)
    
    for i in range(n):
        for j in range(n):
            if visited[i] == False and computers[i][j] == 1:
                answer += 1
                visited[i] = True
                dfs(computers, j)
                
            
    
    return answer