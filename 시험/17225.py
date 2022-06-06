
A,B,N = map(int, input().split())

temp = []
man_count = 0
girl_count = 0
last_time_A = 0
last_time_B = 0
for _ in range(N):
    t,c,m = input().split()
    t = int(t)
    m = int(m)
    if c == 'B':
        if t < last_time_A:
            t = last_time_A
        for i in range(1,m+1):
            temp.append([t,c])
            t = t+A
            last_time_A = t
        man_count+=m
    else:
        if t < last_time_B:
            t = last_time_B
        for i in range(1,m+1):
            temp.append([t,c])
            t = t+B
            last_time_B = t
        girl_count+=m
temp.sort()

man_list = []
girl_list = []
count = 1
for i in temp:
    if i[1] == 'B':
        man_list.append(count)
    else:
        girl_list.append(count)
    count +=1

print(man_count)
for i in man_list:
    print(i, end=' ')
print()
print(girl_count)
for i in girl_list:
    print(i, end=' ')