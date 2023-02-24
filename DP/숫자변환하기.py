def solution(x, y, n):
    answer_num = 0
    # INF로 배열 초기화
    answer = [100000000 for _ in range(1000001)]
    # 시작 지점은 0으로
    answer[x] = 0
    
    for i in range(x,y):
        # 계산이 가능한 숫자라면 최소값으로 계산 bottom-up 방법
        if answer[i] != 100000000:
            if i+n < 1000001:
                answer[i+n] = min(answer[i+n], answer[i]+1)
            if i*2 < 1000001:
                answer[i*2] = min(answer[i*2], answer[i]+1)
            if i*3 < 1000001:
                answer[i*3] = min(answer[i*3], answer[i]+1)
    
    if answer[y] == 100000000:
        answer_num = -1
    else:
        answer_num = answer[y]
    
    return answer_num