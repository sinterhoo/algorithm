from itertools import combinations

def solution(relation):
    answer = 0
    not_list = []
    for i in range(len(relation[0])):
        temp = []
        for j in range(len(relation)):
            if relation[j][i] in temp:
                not_list.append(i)
                break
            else:
                temp.append(relation[j][i])
        else:
            answer +=1
    com_list = []
    for i in range(2,len(not_list)+1):
        com_list += list(combinations(not_list,i))
    answer_list = []
    for i in com_list:
        temp = []
        for j in relation:
            temp_2 = []
            for k in i:
                temp_2.append(j[k])
            if temp_2 in temp:
                break
            else:
                temp.append(temp_2)
        else:
            temp_set = set(i)
            for z in answer_list:
                if z & temp_set == z or z & temp_set == temp_set:
                    break
            else:
                answer +=1
                answer_list.append(temp_set)
    return answer