import sys

m = int(input())

s = [0 for i in range(21)]

for _ in range(m):
    order = sys.stdin.readline().split()
    word = ''
    num = 0
    if len(order) == 2:
        num = int(order[1])
    word = order[0]
    if word == 'add':
        if s[num] == 0:
            s[num] = 1
    elif word == 'remove':
        if s[num] == 1:
            s[num] = 0
    elif word == 'check':
        if s[num] == 1:
            print(1)
        else:
            print(0)
    elif word == 'toggle':
        if s[num] == 1:
            s[num] = 0
        else:
            s[num] = 1
    elif word == 'all':
        for k in range(1,21):
            s[k] = 1
    else:
        for k in range(1,21):
            s[k] = 0
