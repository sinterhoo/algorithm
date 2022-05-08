from dis import dis
import sys
#sys.stdin = open("input.txt", "r")

n,m = map(int, input().split())

m_list = [int(sys.stdin.readline()) for _ in range(m)]

dp = [[0 for _ in range(n+5)] for _ in range(251)]

check = 0
mins = 1e9
def solved(now, distance, count):
    global check
    global mins
    if now > n:
        return -1
    if dp[distance][now] != 0:
        return dp[distance][now]
    if dp[distance][now] == -1:
        return -1
    if now in m_list:
        dp[distance][now] = -1
        return -1
    if now == n:
        check = 1
        mins = min(mins, count)
    dp[distance+1][now + distance+1] = solved(now+distance, distance+1, count+1)
    dp[distance][now + distance] = solved(now+distance, distance, count+1)
    if distance >= 2:
        dp[distance][now + distance - 1] = solved(now+distance, distance-1, count+1)
    return count
a = solved(1,1,0)

for i in dp:
    print(i)

if check == 0:
    print(-1)
else:
    print(mins)