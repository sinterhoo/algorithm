def solution(n, s):
    answer = []
    if s < n:
        answer = [-1]
    else:
        if s % n == 0:
            temp = s//n
            answer = [temp for _ in range(n)]
        else:
            temp = s//n
            answer = [temp for _ in range(n)]
            nums = s%n
            
            while nums != 0:
                for i in range(n):
                    if nums == 0:
                        break
                    answer[i] += 1
                    nums -= 1
            answer.sort()
    return answer