
n,k = map(int, input().split())

nums = input()
stack = []
count = 0

for i in range(0, len(nums)):
    temp = int(nums[i])
    if len(stack) == 0:
        stack.append(temp)
    elif n -i == n-k -len(stack):
        stack.append(temp)
    else:
        while stack:
            if stack[-1] < temp:
                if n - i == n-k -len(stack):
                    stack.append(temp)
                    break
                else:
                    stack.pop()
            else:
                if len(stack) == n-k:
                    break
                else:
                    stack.append(temp)
                    break
        else:
            stack.append(temp)

for i in stack:
    print(i,end='')


# 좀 더 직관적인 코드

""" import sys

n, count = map(int, input().split())
nums = sys.stdin.readline().strip()
stack = []

for i in nums:
    if len(stack) == 0:
        stack.append(i)
    else:
        if not count == 0:
            while stack:
                if int(stack[-1]) < int(i) and count != 0:
                    stack.pop()
                    count = count -1
                else:
                    break
        stack.append(i)

while count !=0:
    stack.pop()
    count = count -1

str1 = ''
for i in stack:
    str1 = str1 + i
print(str1, end='') """
