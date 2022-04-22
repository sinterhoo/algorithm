# 접근 방식 -> 연산 기호는 +와 - 둘 뿐이고 이 때 최소가 되게 하려면 -를 기준으로 괄호를 쳐주면 된다.

import sys

str1 = sys.stdin.readline()

result = 0
stack = []
temp = ''
for i in str1:
    if i == '+':
        result += int(temp)
        temp =''
    elif i == '-':
        result += int(temp)
        stack.append(result)
        temp =''
        result = 0
    else:
        temp += i
else:
    result += int(temp)
    stack.append(result)

start = stack[0]
for i in range(1, len(stack)):
    start -= stack[i]
print(start)