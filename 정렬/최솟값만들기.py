def solution(A,B):
    answer = 0

    A.sort()
    B.sort(reverse=True)
    
    length = len(A)
    for i in range(length):
        answer += A[i]*B[i]
    return answer