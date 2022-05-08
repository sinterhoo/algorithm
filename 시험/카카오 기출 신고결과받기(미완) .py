from collections import defaultdict

def solution(id_list, report, k):
    new_report = set()
    member = set()
    dicts = defaultdict(int)
    answer = [0 for _ in range(len(id_list))]
    report = set(report)
    dicts2 = defaultdict(int)
    for z in range(len(id_list)):
        dicts2[id_list[z]] = z
    for i in report:
        temp = tuple(i.split(' '))
        new_report.add(temp)
        dicts[temp[1]] +=1
        if dicts[temp[1]] >=k:
            member.add(temp[1])
            
    for i in member:
        for j in new_report:
            if j[1] == i:
                answer[dicts2[j[0]]] += 1
            
    
    return answer


result = solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2)