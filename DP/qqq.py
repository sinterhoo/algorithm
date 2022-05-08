import sys

n = int(sys.stdin.readline())
roads = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))
dp = list([0] * (1 << n - 1) for _ in range(n))

print(1 << 3)
print(dp)