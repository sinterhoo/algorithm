def solution(s):
    s = s.lower()
    answer = []
    check = 1
    for word in s:
        if word == ' ':
            check = 1
            answer.append(word)
            continue
        else:
            if check == 1:
                word = word.upper()
                answer.append(word)
                check = 0
            else:
                answer.append(word)
        
    
    return ''.join(answer)