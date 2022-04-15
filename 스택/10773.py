
k = int(input())


num_list = [int(input()) for _ in range(k)]
answer = []
for i in num_list:
    if i != 0:
        answer.append(i)
    else:
        answer.pop()

print(sum(answer))