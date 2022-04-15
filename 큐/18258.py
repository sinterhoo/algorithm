from collections import deque
import sys


N = int(input())


order_list = [sys.stdin.readline().strip() for _ in range(N)]

answer = deque([])
for i in order_list:
    word = i.split(' ')
    if word[0] == 'push':
        answer.append(int(word[1]))
    elif word[0] == 'back':
        if len(answer) >0:
            print(answer[len(answer)-1])
        else:
            print(-1)
    elif word[0] == 'pop':
        if len(answer) > 0:
            print(answer.popleft())
        else:
            print(-1)
    elif word[0] == 'size':
        print(len(answer))
    elif word[0] == 'empty':
        if len(answer) == 0:
            print(1)
        else:
            print(0)
    elif word[0] == 'front':
        if len(answer) >0:
            print(answer[0])
        else:
            print(-1)