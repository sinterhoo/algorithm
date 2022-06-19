def solution(info, query):
    answer = [0 for _ in range(len(query))]
    new_info = []
    new_query = []
    
    for i in info:
        new_info.append(list(i.split(' ')))
    for i in query:
        i = list(i.split(' and '))
        temp = i[3].split(' ')
        i.pop()
        i.append(temp[0])
        i.append(temp[1])
        new_query.append(i)
    index = 0
    for i in new_query:
        for j in new_info:
            for k in range(len(j)):
                if k == 4:
                    if i[k] == '-':
                        continue
                    if int(i[k]) > int(j[k]):
                        break
                    else:
                        continue
                if i[k] == '-':
                    continue
                elif i[k] != j[k]:
                    break
            else:
                answer[index] +=1
        index +=1
    return answer


print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))