def solution(s):
    temp_list = s.split('},')
    new_list = []
    for i in temp_list:
        i = i.replace('{','')
        i = i.replace('}','')
        new_list.append(list(i.split(',')))
    new_list.sort(key = lambda x : len(x))
    answer_temp = []
    answer = []
    for i in new_list:
        for j in i:
            if not int(j) in answer_temp:
                answer.append(int(j))
                answer_temp.append(int(j))
    return answer