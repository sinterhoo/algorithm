# 못품 다익스트라 써서 풀 수 있는듯 어렵;;

maps = [[1,2,2],[3,8,2],[5,3,5]]


def dfs(maps, n):

    down = [n[0]+1, n[1]]
    right = [n[0], n[1]+1]
    if 0<= down[0] < len(maps):
        gap = abs(maps[n[0]][n[1]] - maps[down[0]][down[1]])
        count_1 = dfs(maps, down)
        maxs_1 = max(gap, count_1)
    if 0 <= right[1] < len(maps[0]):
        gap = abs(maps[n[0]][n[1]] - maps[right[0]][right[1]])
        count_2 = dfs(maps, right)
        maxs_2 = max(gap, count_2)
    
    return min(maxs_1, maxs_2)

answer = dfs(maps, [0,0])

print(answer)