from itertools import combinations

## 조합 완탐으로는 실패
def solution(number, k):
    answer = 0
    number = list(number)
    number_com = list(combinations(number,len(number)-k))
    
    
    for i in number_com:
        temp = int(''.join(i))
        answer = max(answer,temp)
        
    return str(answer)