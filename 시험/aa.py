def solution(rooms, target):
    answer = []
    new_rooms =[]
    for i in range(len(rooms)):
        temp = rooms[i].index(']')
        print(rooms[1:temp])
        new_rooms.append(rooms[1:temp], rooms[temp+1:])
    print(new_rooms)
    new_rooms.sort(key = lambda x : abs(int(x[0])-target))
    print(new_rooms)
    
    return answer


x = solution(["[403]James", "[404]Azad,Louis,Andy", "[101]Azad,Guard"],403)