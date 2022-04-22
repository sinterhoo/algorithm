import sys


str1 = sys.stdin.readline().rstrip()
str2 = sys.stdin.readline().rstrip()

maps = [[0 for _ in range(len(str1)+1)] for _ in range(len(str2)+1)]

for i in range(len(str2)+1):
    for j in range(len(str1)+1):
        if i == 0 or j == 0:
            maps[i][j] = 0
            continue
        if str1[j-1] == str2[i-1]:
            maps[i][j] = maps[i-1][j-1] +1
        else:
            maps[i][j] = max(maps[i-1][j], maps[i][j-1])

print(maps[i][j])