# 완전탐색 문제 답게 시간복잡도가 널널했음
# 카드간 3장을 뽑는 경우의 수를 조합으로 구하고
# 해당 조합들 각각의 합을 리스트에 넣은 뒤
# 해당되는 합 중 가장 M 값에 가까운 값을 출력했다.

from itertools import combinations

n,m = map(int, input().split(' '))

answer = list(map(int, input().split(' ')))

answer = list(combinations(answer, 3))

for i in range(len(answer)):
    answer[i] = sum(answer[i])

temp = min(answer)

for k in answer:
    if k > temp and k <= m:
        temp = k

print(temp)
