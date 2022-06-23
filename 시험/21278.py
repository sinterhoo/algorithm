from itertools import combinations


INF = int(1e9)


n,m = map(int, input().split())

graph = [[INF] * (n+1) for _ in range(n+1)]

num_list = [i for i in range(1,n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

comb_list = list(combinations(num_list,2))

answer = INF;
answer_list = []
for i in comb_list:
    temp_answer = 0
    for a in range(1,len(graph)):
        temp = min(graph[a][i[0]]*2,graph[a][i[1]]*2)
        temp_answer += temp
    if answer > temp_answer:
        answer = temp_answer
        answer_list = i
            
print(answer_list[0],answer_list[1],answer)
            
