def solution(brown, yellow):
    answer = []
    # 가로, 세로 시작값
    x = 3
    y = 3
    end = brown // 2
    
    for i in range(x, end+1):
        for j in range(y, end+1):
            temp = 2*i + 2*j -4
            if temp == brown and (i-2)*(j-2) == yellow:
                answer = [i,j]
                break
    
    return answer