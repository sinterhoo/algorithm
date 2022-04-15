import sys

n = int(input())
count =0

list1 = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
list2 = []

for i in range(len(list1)):
    x1 = list1[i][0] - list1[i][1]
    x2 = list1[i][0] + list1[i][1]

    list2.append([0, x1, 0]) # 열리는걸 0 - 그리고 3번쨰 인덱스는 접했는지 안접했는지 체크해주는 상태값
    list2.append([1, x2, 0]) # 닫히는걸 1

list2 = sorted(list2, key = lambda x : (x[1],x[0]))
stack = []

for i in range(len(list2)):
    if len(stack) == 0:
        stack.append(list2[i])
    elif list2[i][0] == 1:
        x = stack.pop()
        if i != len(list2) - 1:
            if len(stack) != 0 and list2[i][1] != list2[i+1][1]:
                stack[-1][2] = 0
        
        count = count + x[2] +1
    else:
        if stack[-1][1] == list2[i][1]:
            stack[-1][2] = 1
        stack.append(list2[i])
count = count +1
print(count)