from collections import defaultdict

def solution(want, number, discount):
    answer = 0
    
    for i in range(len(discount)):
        dicts = defaultdict(int)
        for j in range(i, i+10):
            if j >= len(discount):
                break
            dicts[discount[j]] += 1
        
        for k in range(len(want)):
            if dicts[want[k]] < number[k]:
                break
        else:
            answer += 1
    
    
    return answer