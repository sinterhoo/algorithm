def solution(s):
    answer = 100000
    
    for start in range(1, len(s)+1):
        temp_num = 0
        temp_str = ''
        temp_answer = ''
        
        for i in range(0,len(s),start):
            if temp_str != s[i:i+start]:
                if temp_num == 0:
                    temp_str = s[i:i+start]
                    temp_num = 1
                else:
                    if temp_num != 1:
                        temp_answer += str(temp_num)
                    temp_answer += temp_str
                    temp_str = s[i:i+start]
                    temp_num = 1
            else:
                temp_num +=1
        else:
            if temp_num != 1:
                temp_answer += str(temp_num)
            temp_answer += temp_str
            answer = min(answer, len(temp_answer))
    return answer

print(solution("abcabcdede"))