import sys



n, k = map(int, input().split())

bags = []
answer = [[0 for _ in range(k+1)] for _ in range(n+1)]
for _ in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    bags.append(temp)

for i in range(n+1):
    for j in range(k+1):
        if i == 0 or j == 0:
            answer[i][j] = 0
            continue
        if j >= bags[i-1][0]:
            if j-bags[i-1][0] >=0:
                answer[i][j] = max(answer[i-1][j], answer[i][j-bags[i-1][0]] + bags[i-1][1])
            else:
                answer[i][j] = max(answer[i-1][j], bags[i-1][1])


print(answer[i][j])
