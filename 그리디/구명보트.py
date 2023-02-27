def solution(people, limit):
    answer = 0
    people.sort()
    
    people_count = len(people)
    end_point = 0
    
    # 가장 무거운 사람부터 시작해서 짝이 없으면 end_point 그대로 두고 답 +1
    for i in range(people_count-1, -1, -1):
        if i == end_point:
            answer +=1
            break
        elif i < end_point:
            break
        if people[end_point] + people[i] <= limit:
            answer +=1
            end_point +=1
        else:
            answer +=1
    
    return answer