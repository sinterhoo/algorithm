from cProfile import label


def solution(region, num, info):
    answer = []
    index = 0

    # 인덱스 + 가점 + 청약순위 append
    for i in info:
        i.append(index)
        index +=1
        point = (i[1]+1)*2 +i[2]+2 + (i[3]+1)*5
        i.append(point)
        i.append(0)
    
    # 가점 순으로 sort
    info.sort(key = lambda x : -x[5])
    index = 1

    # 같은 지역부터 청약
    for i in info:
        if num < 1:
            break
        if i[0] == region and i[6] == 0 and num > 0:
            i[6] = index
            index +=1
            num -=1
    
    # 나머지 지역 청약
    if num > 0:
        for i in info:
            if num < 1:
                break
            if i[6] == 0 and num > 0:
                i[6] = index
                index +=1
                num -=1
    
    # 인덱스 순으로 sort
    info.sort(key = lambda x : x[4])

    # 청약 순서 answer에 append
    for i in info:
        if i[6] == 0:
            i[6] = -1
        answer.append(i[6])
    return answer