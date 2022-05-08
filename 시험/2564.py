import sys

m, n = map(int, input().split()) # n 세로 m 가로

shop_num = int(input())
shops = []
for _ in range(shop_num):
    shops.append(list(map(int, sys.stdin.readline().split())))

pos = list(map(int, input().split()))
answer = 0

while shops:
    now = shops.pop()
    if pos[0] == 1:
        if now[0] == 1:                             #  북북
            answer += abs(pos[1] - now[1])          
        elif now[0] == 2:                           #  북남
            answer += min(now[1] + n + pos[1], (m-pos[1]) + n + (m-now[1]) )           
        elif now[0] == 3:                           #  북서
            answer += now[1]+pos[1]
        else:                                       # 북동
            answer+= (m-pos[1]) + now[1]
    elif pos[0] == 2:
        if now[0] == 1:                             # 남북
            answer += min(now[1] + n + pos[1], (m-pos[1]) + n + (m-now[1]) ) 
        elif now[0] == 2:                           # 남남
            answer += abs(now[1]-pos[1])
        elif now[0] == 3:                           # 남서
            answer += pos[1] + (n-now[1])
        else:                                       # 남동
            answer += (m-pos[1]) + (n-now[1])
    
    elif pos[0] == 3:
        if now[0] == 1:                             # 서북
            answer += now[1] + pos[1]
        elif now[0] == 2:                           # 서남
            answer += (n-pos[1]) + now[1]
        elif now[0] == 3:                           # 서서
            answer += abs(now[1] - pos[1])
        else:                                       # 서동
            answer += min(now[1] + m + pos[1], (n-pos[1]) + m + (n-now[1]) )
    else:
        if now[0] == 1:                             # 동북
            answer += pos[1] + (m - now[1])
        elif now[0] == 2:                           # 동남
            answer += (n-pos[1]) + (m-now[1])
        elif now[0] == 3:                           # 동서
            answer += min(now[1] + m + pos[1], (n-pos[1]) + m + (n-now[1]) )
        else:                                       # 동동
            answer += abs(now[1] - pos[1])


print(answer)