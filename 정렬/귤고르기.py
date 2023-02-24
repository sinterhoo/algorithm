from collections import Counter

def solution(k, tangerine):
    tangerine = Counter(tangerine).most_common()
    answer = 0    
    for tanList in tangerine:
        k -= tanList[1]
        answer +=1
        if k <= 0:
            break
    return answer