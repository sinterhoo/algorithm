import sys
from collections import deque

s = sys.stdin.readline().rstrip()

n = int(input())

index = len(s)

left_stack = deque(s)
right_stack = deque()

for _ in range(n):
    temp = list(map(str, input().split()))
    
    if temp[0] == 'L':
        if len(left_stack) == 0:
            continue
        else:
            right_stack.appendleft(left_stack.pop())
    elif temp[0] == 'D':
        if len(right_stack) == 0:
            continue
        else:
            left_stack.append(right_stack.popleft())
    elif temp[0] == 'B':
        if len(left_stack) == 0:
            continue
        else:
            left_stack.pop()
    else:
        left_stack.append(temp[1])

answer = ''.join(left_stack)+''.join(right_stack)

print(answer)