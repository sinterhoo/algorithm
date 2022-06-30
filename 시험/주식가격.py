from collections import deque

def solution(prices):
    answer = deque()
    
    temp = []
    min_temp = []
    min_temp.append([len(prices)-1, prices[-1], 0])
    for i in range(len(prices)):
        temp.append([i,prices[i],0])
    
    while temp:
        temp_num = temp.pop()
        while min_temp:
            temp_min = min_temp.pop()
            if temp_num[1] > temp_min[1]:
                answer.appendleft(temp_min[0]-temp_num[0])
                temp_num = [temp_num[0],temp_num[1],temp_min[0]-temp_num[0]]
                min_temp.append(temp_min)
                min_temp.append(temp_num)
                break
            else:
                if len(min_temp) == 0:
                    answer_num = temp_min[0]-temp_num[0]+temp_min[2]
                    answer.appendleft(answer_num)
                    temp_num = [temp_num[0],temp_num[1],answer_num]
                    min_temp.append(temp_num)
                    break

    answer = list(answer)
        
        
    return answer


print(solution([1, 2, 3, 2, 3, 1]))