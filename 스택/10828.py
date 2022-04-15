import sys

n = int(input())

order_list = [sys.stdin.readline().strip() for _ in range(n)]

answer = []
for i in order_list:
    word = i.split(' ')
    if word[0] == 'push':
        answer.append(int(word[1]))
    elif word[0] == 'top':
        if len(answer) >0:
            print(answer[len(answer)-1])
        else:
            print(-1)
    elif word[0] == 'pop':
        if len(answer) > 0:
            print(answer.pop())
        else:
            print(-1)
    elif word[0] == 'size':
        print(len(answer))
    elif word[0] == 'empty':
        if len(answer) == 0:
            print(1)
        else:
            print(0)