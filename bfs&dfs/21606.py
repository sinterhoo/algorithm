# 시간초과 났던 풀이와 다른점은 실외를 기준으로 인접해있는 실내 노드들을 계산해 연산을 줄이는 것이다.
# 실외를 기준으로 dfs를 돌려 인접한 실내 노드의 개수를 리턴 받고 경로의 수를 계산한다.
# 여기서 생각해야할 것은 실내끼리 붙어있는 경우인데
# 그 경우를 고려해주기 위해 인접 리스트를 선언할 때 count를 2씩 더해준다.

import sys
sys.setrecursionlimit(10**6)

def dfs(node, n, visited, str1, count):
    visited[n] = True

    for i in node[n]:
        if str1[i-1] == '1':
            count = count +1
        elif visited[i] == False and str1[i-1] == '0':
            count = dfs(node, i, visited, str1, count)

    return count

n = int(input())

in_out_check = sys.stdin.readline().rstrip()

node = [[] for _ in range(n+1)]
count = 0
visited = [False]*(n+1)

for i in range(n-1):
    x1,x2 = map(int, sys.stdin.readline().split())
    node[x1].append(x2)
    node[x2].append(x1)
    if in_out_check[x1-1] == '1' and in_out_check[x2-1] == '1':
        count +=2

for i in range(1,n+1):
    if visited[i] == False and in_out_check[i-1] == '0':
        n = dfs(node, i, visited, in_out_check, 0)
        count = count + n*(n-1)


print(count)










# O(N^2)의 풀이 방법 2번, 5번의 경우 시간초과가 난다. (입력값이 매우 커지면)

""" import sys
sys.setrecursionlimit(10**6)

def dfs(node, n, visited, str1):
    global count
    visited[n] = True

    for i in node[n]:
        if visited[i] == False and str1[i-1] == '1':
            count = count +1
        elif visited[i] == False and str1[i-1] == '0':
            dfs(node, i, visited, str1)

n = int(input())

in_out_check = sys.stdin.readline().rstrip()

node = [[] for _ in range(n+1)]
global count
count = 0
for i in range(n-1):
    x1,x2 = map(int, sys.stdin.readline().split())
    node[x1].append(x2)
    node[x2].append(x1)

for i in range(1,n+1):
    if in_out_check[i-1] == '1':
        visited = [False]*(n+1)
        dfs(node, i, visited, in_out_check)


print(count) """