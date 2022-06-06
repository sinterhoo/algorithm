from collections import defaultdict


def findItinerary(tickets):
    tickets.sort()
    dicts = defaultdict(list)
    # 1 -> 나에게 들어오는 수, 2 -> 내가 가는 수
    for i in tickets:
        if len(dicts[i[0]]) == 0:
            dicts[i[0]] = [0,1]
        else:
            dicts[i[0]] = [dicts[i[0]][0], dicts[i[0]][1]+1]
        
        if len(dicts[i[1]]) == 0:
            dicts[i[1]] = [1,0]
        else:
            dicts[i[1]] = [dicts[i[1]][0]+1, dicts[i[1]][1]]
    
    for key, value in dicts.items():
        if value[1] - value[0] >= 0:
            while tickets:
                for i in range(len(tickets)):



findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]])