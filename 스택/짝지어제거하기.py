def solution(s):
    answer = 0
    s = list(s)
    end = len(s)
    prev = []
    prev.append(s[0])
    for i in range(1, end):
        if len(prev) == 0:
            prev.append(s[i])
            continue
        if s[i] == prev[-1]:
            prev.pop()
            continue
        prev.append(s[i])
    
    if len(prev) == 0:
        answer = 1
    
    return answer