from telnetlib import BRK


def solution(n, m, rectangle):
    answer = []

    nums = [[0 for _ in range(n)] for _ in range(m)]

    rectangle.sort(key = lambda x : x[0])

    # 사각형의 개수 40, 좌표 20, 20 완전 탐색해도 충분
    for i in rectangle:
        for _ in range(i[1]):
            check = 0
            for y in range(m):
                for x in range(n):
                    if nums[y][x] == 0 and y+i[0] <= m and x+i[0] <= n:
                        start = [x,y,i[0]]
                        for y_1 in range(y, y+i[0]):
                            for x_1 in range(x, x+i[0]):
                                if nums[y_1][x_1] == 1:
                                    check = 2
                                    break
                            if check == 2:
                                break
                        if check == 2:
                            check = 0
                            continue
                        for y_1 in range(y, y+i[0]):
                            for x_1 in range(x, x+i[0]):
                                nums[y_1][x_1] = 1
                        answer.append(start)
                        check = 1
                        break
                    if check == 1:
                        break
                if check == 1:
                    break
        
    return answer

print(solution(7,8,[[2,2],[1,4],[3,2]]))