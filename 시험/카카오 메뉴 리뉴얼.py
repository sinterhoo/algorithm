from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    answer = []
    temp = defaultdict(int)
    food = defaultdict(list)
    
    for i in orders:
        temp_order = list(i)
        temp_order.sort()
        new_order = []
        for j in course:
            new_order += list(combinations(temp_order,j))
        for k in new_order:
            temp_str = ''.join(k)
            temp[temp_str] +=1
    for key,value in temp.items():
        if value >= 2:
            if len(food[len(key)]) == 0:
                food[len(key)] = [value,key]
            else:
                if food[len(key)][0] == value:
                    food[len(key)] += [value,key]
                elif food[len(key)][0] < value:
                    food[len(key)] = [value,key]

    for i in course:
        if len(food[i]) > 0:
            for k in food[i]:
                if not str(k).isdigit():
                    answer.append(k)
    answer.sort()
    return answer


print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))