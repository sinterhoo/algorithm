import sys
import copy

n = int(input())

one = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

stone = copy.deepcopy(one)
stone.sort(key = lambda x : (x[0], x[2]))

dp = [[1, [], 0] for _ in range(n+1)]

for i in range(n):
    dp[i][1].append(stone[i])
    dp[i][2] = stone[i][1]

for i in range(n):
    for j in range(i): 
        if stone[j][0] < stone[i][0] and stone[j][2] < stone[i][2]:
            if dp[i][0] < dp[j][0] +1 and dp[i][2] < dp[j][2] + stone[j][1] :
                temp = copy.deepcopy(dp[j][1])
                temp.append(stone[i])
                dp[i] = [dp[j][0]+1, temp, dp[j][2] + stone[j][1]]
            else:
                dp[i] = dp[i]
maxs = 0
index = 0
for k in range(len(dp)):
    if dp[k][2] > maxs:
        maxs = dp[k][2]
        index =k
print(dp)
print(dp[index][0])
print(dp[index][1])
for i in dp[index][1]:
    for z in range(len(one)):
        if i == one[z]:
            print(z+1)
