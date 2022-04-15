# 조합을 이용해 완전탐색!!

from itertools import combinations


answer = []
for _ in range(9):
    answer.append(int(input()))

answer = list(combinations(answer, 7))

for k in answer:
    if sum(k) == 100:
        k = list(k)
        k.sort()
        for i in k:
            print(i)
        break