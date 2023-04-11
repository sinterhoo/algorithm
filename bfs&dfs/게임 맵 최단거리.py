from collections import deque

def solution(maps):
    answer = 999999
    n = len(maps)
    m = len(maps[0])
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    def check_range(x,y):
        if x < n and x >= 0 and y < m and y >= 0:
            return True
        else:
            return False
    
    pos = [[-1,0],[1,0],[0,-1],[0,1]]
    q = deque()
    visited[0][0] = True
    q.append([0,0,1])
    while q:
        now = q.popleft()
        if now[0] == n-1 and now[1] == m-1:
                answer = min(answer, now[2])
                continue
        for x,y in pos:
            next_step = [now[0]+x, now[1]+y, now[2]+1]
            if check_range(next_step[0], next_step[1]):
                if visited[next_step[0]][next_step[1]] == False and maps[next_step[0]][next_step[1]] == 1:
                    visited[next_step[0]][next_step[1]] = True
                    q.append(next_step)
        
    if answer == 999999:
        answer = -1
    
    
    
    
    return answer