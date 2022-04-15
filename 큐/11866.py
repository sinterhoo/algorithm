from collections import deque


n,k = map(int, input().split())

list1 = deque([i for i in range(1,n+1)])
answer = []

count = 0
while list1:
    count = count +1
    if count == k:
        answer.append(list1.popleft())
        count = 0
    else:
        temp = list1.popleft()
        list1.append(temp)

print("<", end='')
for i in range(len(answer)):
    if i != len(answer)-1:
        print(answer[i],end=', ')
    else:
        print(answer[i],end=">")