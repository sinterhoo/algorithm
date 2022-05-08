import sys

n,m = map(int, input().split())

nums = list(map(int, sys.stdin.readline().split()))
sums = [0 for _ in range(n)]
for i in range(n):
    sums[i] = sums[i-1] + nums[i]

for _ in range(m):
    i,j = map(int, sys.stdin.readline().split())
    if i == 1:
        print(sums[j-1])
    else:
        print(sums[j-1]-sums[i-2])

