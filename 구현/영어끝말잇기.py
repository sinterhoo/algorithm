import math

def solution(n, words):
    temp = []
    answer = []

    now = 0
    player = 0
    last = ''
    prev = ''
    words_len = len(words)
    
    for i in words:
        now += 1
        if now == words_len:
            last = i
            continue
        if now == 1:
            temp.append(i)
            prev = i[-1]
            continue
        if i in temp or prev != i[0]:
            if now % n == 0:
                player = n
            else:
                player = now % n
            now = math.ceil(now / n)
            break
        else:
            temp.append(i)
            prev = i[-1]
    else:
        if last in temp or prev != last[0]:
            if now % n == 0:
                player = n
            else:
                player = now % n
            now = math.ceil(now / n)
        else:
            player = 0
            now = 0
        
    answer = [player, now]
            
    return answer