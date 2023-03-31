def solution(routes):
    answer = 0
    routes.sort(key = lambda x : (x[1],x[0]))
    temp = []
    for x,y in routes:
        if len(temp) == 0:
            temp.append(y)
            continue
        for i in temp:
            if i >= x and i <= y:
                break
        else:
            temp.append(y)
    return len(temp)