import sys
from collections import defaultdict
print = sys.stdout.write

n,m = map(int, input().split())

password = defaultdict(str)

for _ in range(n):
    homepage,pw = sys.stdin.readline().split()
    password[homepage] = pw

for _ in range(m):
    addr = sys.stdin.readline().rstrip()
    print("%s\n" % password[addr])

