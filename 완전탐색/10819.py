# 문제 링크 : https://www.acmicpc.net/problem/10819
# 완탐이기에 복잡도 충분 (8!) => 약 4만 
# 순서가 필요하기에 조합이 아닌 순열을 이용
# 모든 조합을 리스트에 담고 연산을 진행, 가장 높은 합을 가진 경우의 수를 출력

from itertools import permutations

n = int(input())

answer = list(map(int, input().split(' ')))

answer = list(permutations(answer, n))

answer2 = []
for i in answer:
    result = 0
    for j in range(n-1):
        result = result + abs(i[j] - i[j+1])
    answer2.append(result)

print(max(answer2))

