def numIslands(grid) -> int:
        

        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        
        def dfs(grid, n, visited):
            visited[n[0]][n[1]] = True
            
            pos = [[1,0],[-1,0],[0,1],[0,-1]]
            
            for i in pos:
                next_x = i[0]+n[0]
                next_y = i[1] +n[1]
                if 0<= next_x < len(grid) and 0<= next_y < len(grid[0]):
                    if visited[next_x][next_y] == False and grid[next_x][next_y] == '1':
                        dfs(grid, [next_x,next_y], visited)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j] == False and grid[i][j] == '1':
                    count +=1
                    dfs(grid,[i,j],visited)
                    
        return count

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(numIslands(grid))