def solution(citations):
    temp= 0
    answer = 0
    while temp <= 10000:
        overH = 0
        underH = 0
        for i in citations:
            if i == temp:
                overH +=1
                underH +=1
            elif i < temp:
                underH +=1
            else:
                overH +=1
        
        if overH >= temp and underH <= temp:
            answer = temp
        temp += 1
                
        
    return answer