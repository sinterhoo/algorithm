""" import sys
from collections import deque


name = sys.stdin.readline().rstrip()
name = list(name)
name.sort()
front = []
end = deque([])
check = 0
# 홀수, 짝수 고려

if len(name) % 2 == 0:
    i = 0
    while True:
        if i >= len(name)-1:
            break
        front.append(name[i])   
        end.appendleft(name[i+1])
        i = i+2
else:
    i = 0
    while True:
        if i >= len(name):
            break
        if i == len(name)//2:
            front.append(name[i])
            i=i+1
        else:
            front.append(name[i])
            end.appendleft(name[i+1])
            i=i+2
end = list(end)
end = ''.join(end)
front = ''.join(front)

answer = front+end
temp = answer[::-1]
if answer == temp:
    print(answer)
else:
    print("I'm Sorry Hansoo") """

import sys
from collections import deque

name = sys.stdin.readline().rstrip()

name = list(name)
name.sort()
check = set(name)
name = deque(name)

front = []
end = deque()

count_s = 0
count_list = []
mid = []
for i in check:
    if name.count(i) % 2 != 0:
        count_s +=1
        count_list.append(i)

if count_s > 1:
    print("I'm Sorry Hansoo")
else:
    while name:
        if len(count_list) > 0:
            if count_list[0] == name[0]:
                count_list.pop()
                mid.append(name.popleft())
                continue
        front.append(name.popleft())
        if len(name) == 0:
            break
        end.appendleft(name.popleft())

end = list(end)

answer = front +mid + end
answer = ''.join(answer)
temp = answer[::-1]
if answer == temp:
    print(answer)
else:
    print("I'm Sorry Hansoo")