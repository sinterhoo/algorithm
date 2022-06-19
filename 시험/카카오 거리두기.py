from collections import deque

def bfs(start, maps, visited):
    
    pos = [[1,0],[0,1],[-1,0],[0,-1]]
    
    move = deque()
    move.append(start)
    visited[start[0]][start[1]] = True
    
    while move:
        temp = move.popleft()
        if temp[2] <= 2 and maps[temp[0]][temp[1]] == 'P':
            return False
        
        for i in pos:
            next_mov = [temp[0] + i[0], temp[1]+i[1]]
            if next_mov[0] >= 0 and next_mov[0] < len(maps) and next_mov[1] >= 0 and next_mov[1] < len(maps[0]):
                if visited[next_mov[0]][next_mov[1]] == False:
                    visited[next_mov[0]][next_mov[1]] = True
                    move.append([next_mov[0],next_mov[1],temp[2]+1])
    return True
        

def solution(places):
    answer = []
    for i in places:
        check = 1
        for n in range(len(i)):
            for m in range(len(i[0])):
                if i[n][m] == 'P':
                    visited = [[False for _ in range(len(i[0]))] for _ in range(len(i))]
                    if bfs([n,m,0],i,visited) == False:
                        check = 0
                        break
            if check == 0:
                break
        answer.append(check)
        
    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))