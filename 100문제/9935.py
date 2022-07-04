import sys
from collections import deque

s = sys.stdin.readline().rstrip()
target = list(input())

str1 = deque(s)
stack = []

for _ in range(len(str1)):
    stack.append(str1.popleft())
    if len(stack) >= len(target):
        if stack[-1] == target[-1]:
            index = len(target)
            stack_start = len(stack)-1
            target_start = len(target)-1
            while index != 0:
                if stack_start < 0 or target_start < 0 :
                    break
                if stack[stack_start] != target[target_start]:
                    break
                else:
                    stack_start -=1
                    target_start -=1
                    index -=1
            else:
                for _ in range(len(target)):
                    stack.pop()
else:
    if len(stack) == 0:
        answer = 'FRULA'
    else:
        answer = ''.join(stack)
    print(answer)