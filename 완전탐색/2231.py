

n = int(input())
answer = 1e9
for i in range(n-1, 0, -1):
    temp = str(i)
    tmp_str = 0
    for k in temp:
        tmp_str = tmp_str + int(k)
    temp = tmp_str + i
    if temp == n:
        answer = min(answer, i)
else:
    if answer == 1e9:
        print(0)
    else:
        print(answer)