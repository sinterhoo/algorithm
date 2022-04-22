import sys


str1 = sys.stdin.readline().rstrip()
str2 = sys.stdin.readline().rstrip()

stack = []
for i in str1:
    if i == '4':
        if stack[-1] == 'C':
            stack.pop()
        else:
            stack.append(i)
    else:
        stack.append(i)

temp = ''

for i in stack:
    temp += i

print(temp)
